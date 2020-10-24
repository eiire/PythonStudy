def solution(string, markers):
    strings = []

    while(string.find('\n') != -1):
        strings.append(string[:string.find('\n')])
        string = string[string.find('\n')+1:]

    strings.append(string)

    for marker in markers:
        for i in range(len(strings)):
            strings[i] = strings[i].split(marker)[0].rstrip(' ')

    return '\n'.join(strings)
