# nonoLINE
[![PyPI version](https://badge.fury.io/py/nono-line.svg)](https://badge.fury.io/py/nono-line)<br/>
notify, notify to LINE, short for nonoLINE.<br/>
A simple notification helper to send messages to [LINE Notify](https://notify-bot.line.me/en/).

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
nono_line = nonoLINE('YOUR_ACCESS_TOKEN', max_workers=4)

# Send a test message to LINE Notify.
nono_line.send('test message')

# Send a test message to LINE Notify asynchronously.
nono_line.send('test message', send_async=True)

# Send a test message with a sticker to LINE Notify.
# LINE Sticker list is here, https://devdocs.line.me/files/sticker_list.pdf.
nono_line.send('test message', sticker__id_pkgid=(11, 1))

# Send a test message with a sticker list to LINE Notify.
# A sticker will be selected randomly before sending the message.
nono_line.send('test message', sticker__id_pkgid=[(11, 1), (18, 2), (194, 3), (272, 4)])
```

## Reference
* [LINE Notify API Document](https://notify-bot.line.me/doc/en/)
* [LINE Sticker list](https://devdocs.line.me/files/sticker_list.pdf)

## Version History
* v0.0.3
  * If you pass a sticker list, a sticker will be selected randomly.

* v0.0.2
  * First version release

