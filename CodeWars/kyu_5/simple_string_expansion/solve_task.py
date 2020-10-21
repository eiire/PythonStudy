def solve(st):
    while (st.find('(') != -1):
        start_index = st.rfind('(')
        end_index = st.find(')')
        dilator = st[start_index - 1]
        if dilator.isnumeric():
            st = st[0: start_index - 1] + st[start_index + 1:end_index] * int(dilator) + st[end_index: -1]
        else:
            st = st[0: start_index - 1] + dilator + st[start_index + 1:end_index] + st[end_index: -1]

    return st
