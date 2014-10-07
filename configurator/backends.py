# -*- coding: utf-8 -*-

"""
configurator.types
~~~~~~~~~~~~~~~~~~

This module contains the set of Configurator's backends.

A backend is responsible for retrieving configuration settings from somewhere by
key.

"""

class Backend(object):
    def read(self, key):
        raise NotImplementedError(
            'No read function implemented for %s' % self.__class__.__name__
        )

class DictionaryBackend(Backend):
    pass

class EnvironmentBackend(Backend):
    pass

class EnvironmentFileBackend(Backend):
    pass

class EtcdBackend(Backend):
    pass

class JsonBackend(Backend):
    pass

class ModuleBackend(Backend):
    pass

class PythonFileBackend(Backend):
    pass

class RedisBackend(Backend):
    pass
