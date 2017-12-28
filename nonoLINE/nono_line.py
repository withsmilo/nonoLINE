import re
import requests
import logging
import random
from nonoLINE import InvalidTokenException
from requests_futures.sessions import FuturesSession


def _check_validity(chat_access_token):
    res = requests.get('https://notify-api.line.me/api/status',
                       headers={'Authorization': 'Bearer {}'.format(chat_access_token)}).json()
    if len(res) != 4 or res['message'] != 'ok' or res['status'] != 200:
        raise InvalidTokenException('Failed to check validity. error:{}'.format(res))

    return res['targetType'], res['target'].encode('utf-8')


class nonoLINE:
    def __init__(self, chat_access_token, max_workers=4):
        """Create a new nonoLINE object.

        This class implements a simple notification helper to send some messages to LINE Notify.

        Parameters
        ----------
        chat_access_token : str
            your access token for chat room to notify
        max_workers : int (optional)
            max workers to send some notifications asynchronously
        """
        # Check validity of chat_access_token
        if chat_access_token is None:
            raise InvalidTokenException('Access token is None')
        elif re.match(r'^[0-9a-zA-Z]+$', chat_access_token) is None:
            raise InvalidTokenException('Access token({}) has some non-liternal characters'.format(chat_access_token))
        target_type, target = _check_validity(chat_access_token)
        logging.info('Notification targetType:{}, target:{}'.format(target_type, target))

        self._headers = {'Authorization': 'Bearer {}'.format(chat_access_token),
                         'Content-Type': 'application/x-www-form-urlencoded'}
        self._url = 'https://notify-api.line.me/api/notify'
        self.session = FuturesSession(max_workers=max_workers)

    def send(self, message, sticker__id_pkgid=None, send_async=False):
        """This function send a given message to LINE Notify.

        Parameters
        ----------
        message : str
            your message
        sticker__id_pkgid : tuple(int, int) or list[(int, int)] (optional)
            a specific sticker information, something like (sticker_id, sticker_package_id).
            Sticker information is here, https://devdocs.line.me/files/sticker_list.pdf.
            If you pass a sticker list, a sticker will be selected randomly before sending the message.
        send_async : bool (optional)
            If you would like to send asynchronously, set this to True.
        """
        data = {'message': message}
        if type(sticker__id_pkgid) is tuple and len(sticker__id_pkgid) == 2:
            data.update({'stickerId': sticker__id_pkgid[0], 'stickerPackageId': sticker__id_pkgid[1]})
        elif type(sticker__id_pkgid) is list and len(sticker__id_pkgid) > 0:
            picked = random.choice(sticker__id_pkgid)
            if type(picked) is tuple and len(picked) == 2:
                data.update({'stickerId': picked[0], 'stickerPackageId': picked[1]})

        # Send a message
        try:
            if send_async:
                self.session.post(self._url, headers=self._headers, params=data)
            else:
                res = requests.post(self._url, headers=self._headers, params=data).json()
                if len(res) != 2 or res['message'] != 'ok' or res['status'] != 200:
                    logging.error('Failed to send a message({}) returned result:{}'.format(message, res))
        except requests.RequestException as e:
            logging.error('RequestException: {}'.format(e))
