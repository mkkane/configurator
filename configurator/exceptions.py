# -*- coding: utf-8 -*-

"""
configurator.exceptions
~~~~~~~~~~~~~~~~~~~~~~~

This module contains the set of Configurator's exceptions.

"""

class ConfiguratorException(Exception):
    """
    An ambiguous exception occurred during configuration.
    """

class CoercionError(ConfiguratorException):
    """
    An error occurred when trying to read a value as a given type.
    """
