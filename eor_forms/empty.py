# coding: utf-8


class _Empty(object):

    def __bool__(self):
        return False


empty = _Empty()
