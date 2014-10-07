import configurator
from configurator.types import BoolType, StringType
from configurator.backends import DictionaryBackend, EnvironmentBackend

default = {
    'DEBUG': BoolType(False),
    'SQL_DB_URI': StringType(), # 'postgresql://test:test@localhost/test'
    'REDIS_DB_URI': StringType(), # 'redis://localhost:6379/0'
}

backends = []

config = configurator.create(backends, default)
