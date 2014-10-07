# -*- coding: utf-8 -*-

"""
configurator.types
~~~~~~~~~~~~~~~~~~

This module defines the types that a config setting may take.

"""
from .common import NO_VALUE as _NO_VALUE

class BaseType(object):
    """
    The ...
    """

    def __init__(self, default=_NO_VALUE):
        self.default = default

    def coerce(self, value):
        raise NotImplementedError(
            'No coercion function implemented for %s' % self.__class__.__name__
        )


class BoolType(BaseType):
    pass

class StringType(BaseType):
    pass
