def calculate(data, findall):
    matches = findall(r"([abc])(\+=|-=|=)([abc])?([\+-]?\d+)?")
    for v1, s, v2, n in matches:
        if v2 == '' and s.find('-') != -1:
            data[v1] = data[v1] - int(n or 0)
        if v2 == '' and s.find('+') != -1:
            data[v1] = data[v1] + int(n or 0)
        if v2 == '' and s.find('=') == 0:
            data[v1] = int(n or 0)

        if v2 != '' and s.find('-') != -1:
            data[v1] = data[v1] - (data[v2] + int(n or 0))
        if v2 != '' and s.find('+') != -1:
            data[v1] = data[v1] + (data[v2] + int(n or 0))
        if v2 != '' and s.find('=') == 0:
            data[v1] = data.get(v2, 0) + int(n or 0)

    return data
