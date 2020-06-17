# A B A R --> A got 1/2 students
str_grad = input()
print(len(''.join(filter(lambda ch: ch == 'A', str_grad))) / len(''.join(filter(lambda ch: ch != ' ', str_grad))))