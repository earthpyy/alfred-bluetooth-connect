import os
import sys

from utils import DIR_PATH, FILE_PATH, safe_check_directory, get_value_from_line

command = sys.argv[1]

if command == 'set':  # SET ALIAS
    alias = os.environ['alias']
    device_name = os.environ['device_name']

    str_to_write = '"{}" "{}"\n'.format(alias, device_name)

    # safe check for directory exist
    safe_check_directory(DIR_PATH)

    # write to file
    with open(FILE_PATH, 'ab+') as f:
        f.write(str_to_write)
        sys.stdout.write('Alias has been set!'.format(alias))

elif command == 'unset':  # UNSET ALIAS
    alias = os.environ['alias']

    try:
        with open(FILE_PATH, 'rb+') as f:
            lines = f.readlines()
            f.seek(0)

            found = False
            for line in lines:
                line_alias, _ = get_value_from_line(line)
                # check if alias is match then not write back
                if alias != line_alias:
                    f.write(line)
                else:
                    found = True
            f.truncate()

        if found:
            sys.stdout.write('Alias has been unset!'.format(alias))
    except FileNotFoundError:
        pass
