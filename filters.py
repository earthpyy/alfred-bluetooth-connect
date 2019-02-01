import json
import os
import sys

from utils import FILE_PATH, get_value_from_line, check_set_syntax, split_set_query, return_result


# get argv
command = sys.argv[1]
query = sys.argv[2] if len(sys.argv) > 2 else ''

if command == 'set':  # SET FILTER
    alias, device_name = split_set_query(query)
    valid = check_set_syntax(alias, device_name)

    if valid:
        result = {
            'items': [
                {
                    'title': 'Set alias {} to {}'.format(alias, device_name),
                    'arg': query,
                    'variables': {
                        'alias': alias,
                        'device_name': device_name
                    }
                }
            ]
        }
    else:
        result = {
            'items': [
                {
                    'title': 'Invalid syntax!',
                    'subtitle': 'Syntax: btset {alias} {device name} OR btset {alias} > {device name}'
                }
            ]
        }

    return_result(result)

elif command == 'unset':  # UNSET FILTER
    items = []

    try:
        with open(FILE_PATH, 'rb') as f:
            for line in f:
                alias, device_name = get_value_from_line(line)
                if query in alias:
                    items.append({
                        'title': 'Unset ' + device_name,
                        'arg': query,
                        'variables': {
                            'alias': alias
                        }
                    })
    except EnvironmentError:
        sys.stdout.write(query)

    if items:
        result = {
            'items': items
        }
    else:
        result = {
            'items': [
                {
                    'title': 'Cannot find alias {}'.format(query),
                    'subtitle': 'Please recheck your alias.'
                }
            ]
        }

    return_result(result)

elif command == 'resolve':  # RESOLVE FILTER
    populated_favorite_name = None
    pin = 0

    if query in [None, '']:  # if no query
        favorite_name = os.environ.get('FAVORITE_DEVICE', '')
        if favorite_name == '':  # no favorite device
            items = [
                {
                    'title': 'Toggle',
                    'arg': 'Please specify device alias/name',
                    'subtitle': 'Toggle any bluetooth device'
                }
            ]
        else:  # has favorite device
            items = [
                {
                    'title': 'Toggle ' + favorite_name,
                    'subtitle': 'Toggle favorite bluetooth device',
                    'arg': query,
                    'variables': {
                        'device_name': favorite_name
                    },
                    'mods': {
                        'cmd': {
                            'subtitle': 'Toggle and unmark {} as favorite device'.format(favorite_name)
                        }
                    }
                }
            ]
            pin = 1
            populated_favorite_name = favorite_name

    else:  # query is provided
        items = [
            # default option
            {
                'title': 'Toggle ' + query,
                'arg': query,
                'variables': {
                    'device_name': query
                },
                'mods': {
                    'cmd': {
                        'subtitle': 'Toggle and mark {} as favorite device'.format(query)
                    }
                }
            }
        ]

    try:
        with open(FILE_PATH, 'rb') as f:
            for line in f:
                alias, device_name = get_value_from_line(line)
                if device_name != populated_favorite_name:  # check if favorite name is populated
                    if query == alias:  # pin match on top
                        items.insert(
                            0,
                            {
                                'title': 'Toggle ' + device_name,
                                'arg': query,
                                'variables': {
                                    'device_name': device_name
                                },
                                'mods': {
                                    'cmd': {
                                        'subtitle': 'Toggle and mark {} as favorite device'.format(device_name)
                                    }
                                }
                            }
                        )
                        pin = 1

                    elif query in alias:
                        items.insert(
                            pin,
                            {
                                'title': 'Toggle ' + device_name,
                                'arg': query,
                                'variables': {
                                    'device_name': device_name
                                },
                                'mods': {
                                    'cmd': {
                                        'subtitle': 'Toggle and mark {} as favorite device'.format(device_name)
                                    }
                                }
                            }
                        )

        result = {
            'items': items
        }
        return_result(result)
    except EnvironmentError:
        sys.stdout.write(query)
