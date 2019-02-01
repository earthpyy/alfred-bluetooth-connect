from os import makedirs
from os.path import expanduser, isdir


# variables
ALFRED_VERSION = '3'
BUNDLE_ID = 'com.earthpyy.bluetooth.connect'
FILE_NAME = 'alias.txt'

DIR_PATH = '{}/Library/Application Support/Alfred {}/Workflow Data/{}'.format(expanduser('~'), ALFRED_VERSION, BUNDLE_ID)
FILE_PATH = DIR_PATH + '/' + FILE_NAME


# functions
def split_set_sentence(sentence):
    if '>' in query:  # long type
        split_words = query.split('>')

        alias = split_words[0].strip()
        name = split_words[1].strip() if len(split_words) > 1 else None

    else:  # short type
        split_words = query.split(' ')

        alias = split_words[0]
        name = ' '.join(split_words[1:]) if len(split_words) > 1 else None

    return alias, name

def safe_check_directory(path):
    try:
        makedirs(DIR_PATH)
    except OSError:
        if not isdir(DIR_PATH):
            raise

def get_value_from_line(line):
    separator = '" "'
    split_line = line.split(separator)

    alias = split_line[0][1:]  # remove left double quote
    name = split_line[1][:-2]  # remove right double quote and newline

    return alias, name
