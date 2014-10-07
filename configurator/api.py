# -*- coding: utf-8 -*-

"""
configurator.api
~~~~~~~~~~~~~~~~

This module implements the Configurator API.

"""


def create(backends, default):
    """
    ...
    """
    return Configurator(backends, default).read_to_dict()
