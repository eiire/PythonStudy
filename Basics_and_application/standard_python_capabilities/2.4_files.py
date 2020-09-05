
"""
Task 1

Пример входного файла:
    ab
    c
    dde
    ff
"""


def task_1():
    lines = []
    file = open('input_f.txt', 'r')
    file2 = open('res_f.txt', 'w')

    for line in file:
        lines.append(line.replace('\n', ''))
    print(lines)

    for line in reversed(lines):
        file2.write(line)
        file2.write('\n')
    file.close()
    file2.close()


# Find files in directories
def task_2():
    import os
    res_file = open('res_f.txt', 'w')
    folder = input("Input name folder for work: ")
    catch_py = 0
    for current_dir, dirs, files in os.walk(folder):
        for file in files:
            if (file.rfind('y') == len(file) - 1) and catch_py != 1:
                catch_py = 1
                res_file.write(current_dir)
                res_file.write('\n')
        catch_py = 0
    res_file.close()


# Task 3 LAMBDA
def mod_checker(x, mod=0):
    return lambda y: y % x == mod

# task_1()
# task_2()