# nonoLINE
[![PyPI version](https://badge.fury.io/py/nono-line.svg)](https://badge.fury.io/py/nono-line)<br/>
notify, notify to LINE, short for nonoLINE.<br/>
A simple notification helper to send messages to [LINE Notify](https://notify-bot.line.me/en/), which supports REST API interfaces which can be accessed with the access token acquired in advance. With nonoLINE, you are able to send some messages to a chat room of LINE with ease in your Python environment!

## Getting Started
1. nonoLINE supports both Python2 and Python3. If you would like to install nonoLINE, just use pip like below.
```shell
$ pip install nono-line
```
2. Login to [the mypage of LINE Notify](https://notify-bot.line.me/my/). If you are not LINEr yet, register to it as a new user.
3. Generate an access token for a specific chat and memorize it.

## Usage
```python
# Import Python library
from nonoLINE import nonoLINE

# Create a new nonoLINE object.
nono_line = nonoLINE('YOUR_ACCESS_TOKEN', max_workers=4, default_tag='TEST1')

# Send a test message to LINE Notify.
nono_line.send('test message')

# Send a test message to LINE Notify with a specific tag.
nono_line.send('test message', tag='TEST2')

# Send a test message to LINE Notify asynchronously.
nono_line.send('test message', send_async=True)

# Send a test message with a sticker to LINE Notify.
# LINE Sticker list is here, https://devdocs.line.me/files/sticker_list.pdf.
# sticker__id_pkgid is a tuple (STKID, STKPKGID).
nono_line.send('test message', sticker__id_pkgid=(11, 1))

# Send a test message with a sticker list to LINE Notify.
# sticker__id_pkgid is able to set as a list of tuple (STKID, STKPKGID).
# In this case, a sticker will be selected randomly before sending the message.
nono_line.send('test message', sticker__id_pkgid=[(11, 1), (18, 2), (194, 3), (272, 4)])
```

## API Rate Limit
The limit of API calls per hour is set to 1000. The limit is per access token.

## Reference
* [LINE Notify API Document](https://notify-bot.line.me/doc/en/)
* [LINE Sticker list](https://devdocs.line.me/files/sticker_list.pdf)

## Version History
* 2019.05.02 : v0.0.6
  * Handle some error cases of *requests*.

* 2018.01.24 : v0.0.5
  * Add a tag to your message if needed.

* 2017.12.29 : v0.0.4
  * Set a parent class(object) to nonoLINE.

* 2017.12.28 : v0.0.3
  * If you pass a sticker list to send(), a sticker will be selected randomly.

* 2017.12.27 : v0.0.2
  * First version release

