from configparser import ConfigParser

parser = ConfigParser()
parser.read('dev.ini')

print(parser.sections())

for value in parser['settings']:
    print(value)