from bs4 import BeautifulSoup


def parse(path_to_file):
    res = [0, 0, 0, 0]
    wiki_file = open(path_to_file, 'r', encoding='utf-8')
    soup = BeautifulSoup(wiki_file, 'lxml')

    all_img_200(res, soup)
    count_titles(res, soup)
    find_a(res, soup)
    sub_lists(res, soup)

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
        'h6': 0,
    }

    for h_n, count in all_title.items():
        for title in soup(h_n):
            try:
                if title.find_parent(id="bodyContent").name == 'div':
                    try:
                        if str(type(title.string)) == "<class 'bs4.element.NavigableString'>":
                            if title.string[0] == 'E' or title.string[0] == 'T' or title.string[0] == 'C':
                                res[1] += 1
                        else:
                            new_tag = title.next
                            while str(type(new_tag.string)) != "<class 'bs4.element.NavigableString'>":
                                new_tag = new_tag.next

                            if new_tag.string[0] == 'E' or new_tag.string[0] == 'T' or new_tag.string[0] == 'C':
                                res[1] += 1

                    except TypeError:
                        pass  # empty title
            except AttributeError:
                pass  # no div with att bodyContent above

    # print(res)


def find_a(res, soup):
    res_count = 0
    for tag in soup('a'):
        try:
            counter = 1
            if tag.find_parent(id="bodyContent").name == 'div':
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


def sub_lists(res, soup):
    counter = 0

    for tag in soup('ul'):
        try:
            if tag.find_parent(id="bodyContent").name == 'div':
                counter += 1
                # print(tag.name)
                try:
                    if tag.find_parent("ol").name == "ol":
                        counter -= 1
                except AttributeError:
                    pass

                try:
                    if tag.find_parent("ul").name == "ul":
                        counter -= 1
                except AttributeError:
                    pass
        except AttributeError:
            pass

    for tag in soup('ol'):
        try:
            if tag.find_parent(id="bodyContent").name == 'div':
                counter += 1
                # print(tag.name)
                try:
                    if tag.find_parent("ol").name == "ol":
                        counter -= 1
                        # print(tag.name, "<-- -1 ol")
                except AttributeError:
                    pass

                try:
                    if tag.find_parent("ul").name == "ul":
                        counter -= 1
                        # print(tag.name, "<-- -1 ul")
                except AttributeError:
                    pass
        except AttributeError:
            pass

    res[3] = counter