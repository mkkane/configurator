import pprint
from pygments import highlight
from pygments.lexers import Python3Lexer
from pygments.formatters import TerminalFormatter

import exampleapp

config_dict = exampleapp.config.to_dict()
config_str = pprint.pformat(config_dict, indent=2)

print('Example App Config'.center(80, '-'))
print()
print(highlight(config_str, Python3Lexer(), TerminalFormatter()))
print(''.center(80, '-'))
