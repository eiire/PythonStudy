"""This problem takes its name by arguably the most important event in the life of the ancient historian kyu_5:
according to his tale, he and his 40 soldiers were trapped in a cave by the Romans during a siege.

Refusing to surrender to the enemy, they instead opted for mass suicide, with a twist: they formed a circle and
proceeded to kill one man every three, until one last man was left (and that it was supposed to kill himself to
end the act)."""


def josephus(items, k):
    new_arr = list()

    while len(items) != 0:
        if k > len(items):
            res = items[k % len(items) - 1]
        else:
            res = items[k - 1]

        items = items[items.index(res):] + items[:items.index(res)]
        items.remove(res)
        new_arr.append(res)

    return new_arr


"""Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an
array with words. You should return an array of all the anagrams or an empty array if there are none. For example:"""


def anagrams(_word, words):
    # Create dict chars
    word_dict = create_inf_word(_word)

    res_list = list()
    for word in words:
        for k, v in word_dict.items():
            if k == 'len': break

            if word.count(k) == v and len(word) == word_dict['len'] and word not in res_list:
                res_list.append(word)
            elif word.count(k) != v:
                try:
                    res_list.remove(word)
                except ValueError:
                    pass

                break

    return res_list


def create_inf_word(word):
    word_dict = dict()
    for element in word:
        if element in word_dict.keys():
            word_dict[element] += 1
        else:
            word_dict.update({element: 1})
    word_dict.update({'len': len(word)})

    return word_dict


"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in 
a human-readable format (HH:MM:SS)
"""


def make_readable(seconds):
    if len(str(seconds % 60)) == 1:
        sec = '0' + str(seconds % 60)
    else:
        sec = str(seconds % 60)

    if len(str(seconds // 60 % 60)) == 1:
        _min = '0' + str(seconds // 60 % 60)
    else:
        _min = str(seconds // 60 % 60)

    if len(str(seconds // 3600)) == 1:
        hour = '0' + str(seconds // 3600)
    else:
        hour = str(seconds // 3600)

    return hour + ':' + _min + ':' + sec


"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks 
untouched.
"""


def pig_it(text):
    print(text)
    return ' '.join([checker(new_word) for new_word in text.split(' ')])


def checker(word):
    if word == '?' or word == '!':
        return word
    else:
        return word[1:] + word[0:1] + 'ay'


if __name__ == '__main__':
    # print(josephus(["C","o","d","e","W","a","r","s"],4))
    # print(make_readable(86399))
    print(pig_it('Pig latin is cool ?'))
    pass
