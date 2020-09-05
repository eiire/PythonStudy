import csv


check_dict = {}
n = 0
with open("Crimes.csv") as f:
    _dict = csv.DictReader(f)
    for row in _dict:
        n += 1
        check_dict.update({row['Primary Type']: n})

res = 0
for el in check_dict.values():
    if el > res:
        res = el

print(res)
print(check_dict)