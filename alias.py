import sys

from utils import DIR_PATH, FILE_PATH, split_set_sentence, safe_check_directory, get_value_from_line


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
