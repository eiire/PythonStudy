from bs4 import BeautifulSoup
import unittest
from lxml import *


def parse(path_to_file):
    res = [0, 0, 0, 0]
    wiki_file = open(path_to_file, 'r', encoding='utf-8')
    soup = BeautifulSoup(wiki_file, 'lxml')

    all_img_200(res, soup)
    count_titles(res, soup)
    find_a(res, soup)

    wiki_file.close()
    return res


def all_img_200(res, soup):
    all_img = soup('img')
    for img in all_img:
        if int(img.get('width', '0')) >= 200:
            res[0] += 1


def count_titles(res, soup):
    all_title = {
        'h1': 0,
        'h2': 0,
        'h3': 0,
        'h4': 0,
        'h5': 0,
        'h6': 0
    }

    for h_n, count in all_title.items():
        for title in soup(h_n):
            # print(title.next.string, h_n)
            try:
                if title.find_parent(id="bodyContent").name == 'div':
                    try:
                        #  <h1><span>text</span></h> !NO MORE!
                        if (title.next.string[0] == 'E' or title.next.string[0] == 'T' or title.next.string[0] == 'C'):
                            res[1] += 1
                    except TypeError:
                        pass  # empty title
            except AttributeError:
                pass  # no div with att bodyContent above

def find_a(res, soup):
    res_count = 0
    for tag in soup('a'):
        try:
            if tag.find_parent(id="bodyContent").name == 'div':
                counter = 1
                try:
                    new_tag = tag
                    while new_tag.find_next_sibling().name == 'a':
                        new_tag = new_tag.find_next_sibling()
                        counter += 1
                        # print(new_tag.name)
                    # print("\n")
                except:
                    pass
                if res_count < counter: res_count = counter
        except AttributeError:
            pass  # no div with att bodyContent above
    res[2] = res_count


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                res = parse(path)
                self.assertEqual(res[0], expected[0])
                self.assertEqual(res[1], expected[1])
                self.assertEqual(res[2], expected[2])


if __name__ == '__main__':
    unittest.main()
    # parse('wiki/Spectrogram')