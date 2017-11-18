import logging
import sys

PY3 = sys.version_info[0] == 3

if PY3:
    text_type = str

    def iso_8859_1(s):
        return s

    def unicode_repr(s):
        return repr(s)
else:
    text_type = unicode  # noqa

    def iso_8859_1(s):
        return s.decode('latin-1')

    def unicode_repr(s):
        if isinstance(s, unicode):  # noqa
            return repr(s)[1:]
        else:
            return repr(s)


class NullHandler(logging.Handler):
    """
    This handler does nothing. It's intended to be used to avoid the
    "No handlers could be found for logger XXX" one-off warning.
    """
    def handle(self, record):
        pass

    def emit(self, record):
        pass

    def createLock(self):
        self.lock = None
