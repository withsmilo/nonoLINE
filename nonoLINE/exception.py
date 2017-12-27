
class NonoLineException(Exception):
    def __init__(self, message, *args):
        self.message = message
        super(Exception, self).__init__(message, args)


class InvalidTokenException(NonoLineException):
    def __init__(self, message, *args):
        self.message = '[InvalidToken] {}'.format(message)
        super(InvalidTokenException, self).__init__(message, *args)