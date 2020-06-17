# My version
print("Please input text:")
text_input = input()
text_input = text_input.replace('.', '')

# print(text_input)
count_words = {}

# count freq words in string
for word in text_input.split(' '):
    if word in count_words:
        count_words[word] += 1
    else:
        count_words.update({word : 1})
print(count_words)
list_words = ['' for i in count_words]
i = 0
for key in count_words.keys():
    list_words[i] += key
    i += 1


list_words = [len(word) for word in list_words]
new_dict = {}
i = 0
for key in count_words:
    new_dict.update({list_words[i] : count_words.get(key)})  # bug
    i += 1

for key in sorted(new_dict):
    print("%s : %s" % (key, new_dict[key]))

# For stepik
print("\n")
count_words = {}

for word in text_input.split(' '):
    if len(word) in count_words:
        count_words[len(word)] += 1
    else:
        count_words.update({len(word) : 1})

for key in sorted(count_words):
    print("%s : %s" % (key, count_words[key]))