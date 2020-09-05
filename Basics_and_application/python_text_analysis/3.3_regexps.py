import re
import sys

sys.stdin = open("for_reg.txt")

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


def task_7():

    pattern = r"\b[aA]+\b"
    for line in sys.stdin:
        print(re.sub(pattern, "argh", line, 1))


def task_8():
    for line in sys.stdin:
        work_word = re.sub(r"(\b\w)(\w)", r"\2\1", line)
        print(work_word.strip())


def task_9():
    for line in sys.stdin:
        work_word = re.sub(r"(\w)(\1+)", r"\1", line)
        print(work_word.strip())


task_9()