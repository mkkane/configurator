import logging
import types
import json
import os

logger = logging.getLogger(__name__)

class Config(object):

    def __init__(self, settings_obj):
        # If we were not passed a dict, lets get the dict from it.
        # TODO: make this safe for objects that don't have __dict__.
        if not isinstance(settings_obj, dict):
            settings_dict = settings_obj.__dict__
        else:
            settings_dict = settings_obj

        # Import only upper case keys from the given object.
        settings = {
            key: value for key, value in settings_dict.items() if key.isupper()
        }

        self._settings = settings

        # If this was config from a module, get the name of it and try to load
        # any corresponding settings.json file.
        if isinstance(settings_obj, types.ModuleType):
            settings_filename = settings_obj.__name__.split('.')[-1] + '.json'
            with open(self.get_instance_relative_path(settings_filename)) as f:
                instance_config = Config.from_json(f.read())
            self.update(instance_config)

        # If desired, warn / raise exception for any unset values.
        # TODO

    @classmethod
    def set_instance_dir(cls, directory):
        cls._instance_dir = os.path.join(directory, '')
    
    def get_instance_relative_path(self, path):
        return os.path.join(self._instance_dir, path)

    @classmethod
    def from_json(cls, settings_json):
        try:
            settings_dict = json.loads(settings_json)
            if not isinstance(settings_dict, dict):
                raise Error('JSON must be an object (dict)')
        except (Error, ValueError) as exc:
            raise BadJsonError(str(exc))
        return cls(settings_dict)

    def to_dict(self):
        return self._settings

    def to_json(self):
        return json.dumps(self.to_dict())

    def get(self, key, default=None):
        return self._settings.get(key, default)

    def update(self, settings):
        if isinstance(settings, Config):
            self._settings.update(settings.to_dict())
        else:
            self._settings.update(Config(settings))
        return self

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self.to_dict())


class Error(Exception):
    pass

class BadJsonError(Error):
    pass
