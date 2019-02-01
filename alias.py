import sys
from os import makedirs
from os.path import expanduser, isdir


# variables
ALFRED_VERSION = '3'
BUNDLE_ID = 'com.earthpyy.bluetooth.connect'
FILE_NAME = 'alias.txt'

DIR_PATH = '{}/Library/Application Support/Alfred {}/Workflow Data/{}'.format(expanduser('~'), ALFRED_VERSION, BUNDLE_ID)
FILE_PATH = DIR_PATH + '/' + FILE_NAME


# get query
query = sys.argv[1]

# verify syntax with ">"
if '>' in query:  # long type
    split_words = query.split('>')

    alias = split_words[0].strip()
    name = split_words[1].strip()

else:  # short type
    split_words = query.split(' ')

    alias = split_words[0]
    name = ' '.join(split_words[1:])

# create alias result
result = '"{}" "{}"\n'.format(alias, name)

# safe check for directory exist
try:
    makedirs(DIR_PATH)
except OSError:
    if not isdir(DIR_PATH):
        raise

# write to file
with open(FILE_PATH, 'ab+') as f:
    f.write(result)
    sys.stdout.write(result)
