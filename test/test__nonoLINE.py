import time
from datetime import datetime
import logging
from nonoLINE import nonoLINE


def print_elapsed_time(func, *args, **kwargs):
    t_start = time.time()
    result = func(*args, **kwargs)
    elapsed = time.time() - t_start
    name = func.__name__
    arg_list = []
    if args:
        arg_list.append(', '.join(repr(arg) for arg in args))
    if kwargs:
        pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
        arg_list.append(', '.join(pairs))
    arg_str = ', '.join(arg_list)
    logging.info('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)-08s [%(filename)s:%(lineno)s] %(message)s',
                        level=logging.INFO)

    nono_line = nonoLINE('YOUR_ACCESS_TOKEN')
    time_format = '%Y%m%d - %H%M%S.%f'

    logging.info('Send a test message to LINE')
    print_elapsed_time(nono_line.send,
                       '\n[1] This is a test message.\ncurrent time:{}'.format(datetime.now().strftime(time_format)[:-3]))

    logging.info('Send a test message to LINE asynchronously')
    print_elapsed_time(nono_line.send,
                       '\n[2] This is a test message.\ncurrent time:{}'.format(datetime.now().strftime(time_format)[:-3]),
                       send_async=True)

    logging.info('Send a test message with a sticker to LINE')
    print_elapsed_time(nono_line.send,
                       '\n[3] This is a test message.\ncurrent time:{}'.format(datetime.now().strftime(time_format)[:-3]),
                       sticker__id_pkgid=(11, 1))

    logging.info('Send a test message with a sticker random list to LINE')
    print_elapsed_time(nono_line.send,
                       '\n[4] This is a test message.\ncurrent time:{}'.format(datetime.now().strftime(time_format)[:-3]),
                       sticker__id_pkgid=[(11, 1), (18, 2), (194, 3), (272, 4)])
