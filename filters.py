import json
import sys

from variables import FILE_PATH


# funcions
def get_value_from_line(line):
    separator = '" "'
    split_line = line.split(separator)

    alias = split_line[0][1:]  # remove left double quote
    name = split_line[1][:-2]  # remove right double quote and newline

    return alias, name


# get argv
command = sys.argv[1]
query = sys.argv[2] if len(sys.argv) > 2 else ''

if command == 'resolve':  # RESOLVE ALIAS
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
