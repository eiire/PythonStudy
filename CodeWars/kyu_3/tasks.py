class Calculator(object):
    def evaluate(self, string):
        list_string = string.split(' ')
        while len(list_string) != 1:
            if '*' in list_string:
                index_operation = list_string.index('*')
                res_operation = float(list_string[index_operation - 1]) * float(list_string[index_operation + 1])
                list_string.pop(index_operation)
                list_string.pop(index_operation)
                list_string[index_operation - 1] = res_operation

            if '/' in list_string:
                index_operation = list_string.index('/')
                res_operation = float(list_string[index_operation - 1]) / float(list_string[index_operation + 1])
                list_string.pop(index_operation)
                list_string.pop(index_operation)
                list_string[index_operation - 1] = res_operation

            if '-' in list_string:
                index_operation = list_string.index('-')
                res_operation = float(list_string[index_operation - 1]) - float(list_string[index_operation + 1])
                list_string.pop(index_operation)
                list_string.pop(index_operation)
                list_string[index_operation - 1] = res_operation

            if '+' in list_string:
                index_operation = list_string.index('+')
                res_operation = float(list_string[index_operation - 1]) + float(list_string[index_operation + 1])
                list_string.pop(index_operation)
                list_string.pop(index_operation)
                list_string[index_operation - 1] = res_operation

        return float(list_string[0])

if __name__ == '__main__':
    res = Calculator().evaluate("1.1 + 2.2 + 3.3")
    print(res)