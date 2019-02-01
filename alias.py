import json
import sys
from os import makedirs
from os.path import expanduser, isdir

from variables import DIR_PATH, FILE_PATH


# funcions
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


# get argv
command = sys.argv[1]
query = sys.argv[2] if len(sys.argv) > 2 else ''

if command == 'set':  # SET ALIAS
    alias, name = split_set_sentence(query)

    # check syntax
    valid = check_set_syntax(alias, name)

    if valid:
        result = '"{}" "{}"\n'.format(alias, name)

        # safe check for directory exist
        safe_check_directory(DIR_PATH)

        # write to file
        with open(FILE_PATH, 'ab+') as f:
            f.write(result)
            sys.stdout.write('Alias \'{}\' has been set!'.format(alias))

elif command == 'unset':  # UNSET ALIAS
    # open file
    try:
        with open(FILE_PATH, 'rb+') as f:
            lines = f.readlines()
            f.seek(0)

            found = False
            for line in lines:
                alias, _ = get_value_from_line(line)
                # check if alias is match then not write back
                if alias != query:
                    f.write(line)
                else:
                    found = True
            f.truncate()

        if found:
            sys.stdout.write('Alias \'{}\' has been unset!'.format(alias))
    except FileNotFoundError:
        pass

elif command == 'resolve':  # RESOLVE ALIAS
    items = [
        # default option
        {
            'title': 'Toggle ' + query,
            'arg': query
        }
    ]

    # open file
    try:
        with open(FILE_PATH, 'rb') as f:
            for line in f:
                alias, name = get_value_from_line(line)
                if query in alias:
                    items.append({
                        'title': 'Toggle ' + name,
                        'arg': name
                    })

        result = {
            'items': items[::-1]  # reverse result
        }
        sys.stdout.write(json.dumps(result))
    except EnvironmentError:
        sys.stdout.write(query)
