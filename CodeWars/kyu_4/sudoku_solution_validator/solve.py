def valid_solution(board):
    res = True
    for j in range(len(board)):
        check = []
        for x_list in board:
            for y_el in x_list[j:j + 1]:
                check.append(y_el)
                if check.count(y_el) > 1:
                    res = False

    if res is True:
        for j in range(len(board)):
            check_2 = []
            for x_list in board:
                for y_els in split(x_list)[j // 3:j // 3 + 1]:
                    check_2.append(y_els)
                    if len(check_2) > 3:
                        check_2 = check_2[3:]
                    if len(check_2) == 3 and res is True:
                        res = is_valid(check_2)

    return res


def is_valid(matrix):
    group = []
    for el in matrix:
        group += el
    res = True
    for el in range(10):
        res = False if group.count(el) > 1 else True
    return res


def split(arr):
    return [arr[0:3], arr[3:6], arr[6:9]]
