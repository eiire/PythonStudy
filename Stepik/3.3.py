import re
import sys


def task_1():
    pattern = r"cat"
    work_line = ""

    counter = 0
    for line in sys.stdin:
        work_line = re.findall(pattern, line.replace('\n', ''))
        for el in work_line:
            if pattern == el:
                counter += 1
                if counter == 2:
                    print(line.replace('\n', ''))
        counter = 0
    return 0


def task_2():
    pattern = r"\bcat\b"
    for line in sys.stdin:
        lst_word = line.split(' ')
        for word in lst_word:
            if re.search(pattern, word):
                print(line)
                break
        lst_word.clear()


def task_3():
    pattern = r"z[\w]{3}z"
    for line in sys.stdin:
        if re.search(pattern, line):
            print(line)


def task_4():
    pattern = r"\\"
    for line in sys.stdin:
        if re.search(pattern, line):
            print(line.strip())


#  ggr blabla gfwg
#  eherh heth
def task_5():
    pattern = r"\b(\w+)\1\b"
    work_lst = []
    for line in sys.stdin:
        work_lst = line.split(' ')
        str = ''.join(work_lst[len(work_lst) - 1:]).strip()
        work_lst.pop()
        work_lst.append(str)
        for word in work_lst:
            if re.search(pattern, word):
                print(re.search(pattern, word))
                print(line)
                break


def task_6():
    pattern = r"\bhuman\b"
    for line in sys.stdin:
        print(re.sub(pattern, 'computer', line).strip())

# task_6()
# task_5()
# task_4()
# task_3()
# task_2()
# task_1()