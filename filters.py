import json
import sys

from utils import FILE_PATH, get_value_from_line


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
