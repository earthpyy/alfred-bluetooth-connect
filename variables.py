from os.path import expanduser


# variables
ALFRED_VERSION = '3'
BUNDLE_ID = 'com.earthpyy.bluetooth.connect'
FILE_NAME = 'alias.txt'

DIR_PATH = '{}/Library/Application Support/Alfred {}/Workflow Data/{}'.format(expanduser('~'), ALFRED_VERSION, BUNDLE_ID)
FILE_PATH = DIR_PATH + '/' + FILE_NAME
