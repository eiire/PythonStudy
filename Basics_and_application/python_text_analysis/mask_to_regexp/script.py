import csv
import os


def all_except(new_numbers):
    old_group = ""
    for v in new_numbers.values():
        old_group += '\\' + str(v)
    return old_group


def to_valid_mask(row):
    for ch in list(row):
        if ch.isdigit():
            yield ch
        else:
            yield ch.upper()


def gen_regexp(path):
    control_ch = {
        # ch mask : group link (counter_group)
    }
    regexp = ""
    counter_group = 2
    new_pattern = True

    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            regexp += "(.){3}"
            for ch in to_valid_mask(row[0]):
                if new_pattern and not ch.isdigit():
                    new_pattern = False
                    regexp += "(\\d)"
                    control_ch[ch] = counter_group
                    continue

                if not ch.isdigit() and ch not in control_ch.keys():
                    counter_group += 1
                    regexp += f"([^{all_except(control_ch)}])"
                    control_ch[ch] = counter_group
                elif not ch.isdigit():
                    regexp += f"\\{control_ch[ch]}"
                else:
                    regexp += f"[{ch}]"

            new_pattern = True
            regexp += '\n'
            counter_group = 2
            control_ch = {}

    res_file_path = os.path.abspath(os.curdir) + "/regexps.txt"
    with open(res_file_path, 'w') as res_regexps:
        res_regexps.write(regexp)


if __name__ == "__main__":
    print("In order to translate the masks into a regular expressions, you must enter the absolute path to the file [1]\
or put the file in the same folder where the script was run [2]:\n")
    print("To exit enter exit.")

    while True:
        mode = input("Please input variant number [1 or 2 or exit]: ")
        if mode == '1':
            path = input('Path to file: ')

            if os.path.exists(path):
                gen_regexp(path)
                print("\nThe regular expressions file is located in the folder where the script was run.")
                break
            else:
                print('\nFile does`t exists. Try again.')
        elif mode == '2':
            name = input('File name: ')
            path = os.path.abspath(os.curdir) + '/' + name

            if os.path.exists(path):
                gen_regexp(path)
                print("\nThe regular expressions file is located in the folder where the script was run.")
                break
            else:
                print('\nFile does`t exists. Try again.')
        elif mode == 'exit':
            break
        else:
            continue
