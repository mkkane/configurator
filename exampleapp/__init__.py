import os

from configurator import Config
from . import settings

Config.set_instance_dir(os.path.dirname(__file__) + '/../instance')
config = Config(settings)
