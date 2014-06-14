import json

def from_dict(settings_dict):
    return settings_dict

def from_module(settings_module):
    settings_dict = {
        k:v for k,v in settings_module.__dict__.items() if not k.startswith('__')
    }
    return from_dict(settings_dict)

def from_json(settings_json):
    try:
        settings_dict = json.loads(settings_dict)
        if not isinstance(settings_dict, dict):
            raise Error('JSON must be an object (dict)')
    except (Error, ValueError) as exc:
        raise BadJsonError(exc.msg)

    return from_dict(settings_dict)


class Error(Exception):
    pass

class BadJsonError(Error):
    pass
