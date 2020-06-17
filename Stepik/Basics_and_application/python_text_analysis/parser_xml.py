from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XMLParser

xml_code = """<cube color="blue"><cube color="red"><cube color="green"><cube color="green"><cube color="green"><cube color="blue"></cube><cube color="green"></cube><cube color="red"></cube></cube></cube></cube></cube><cube color="red"><cube color="blue"></cube></cube></cube>"""


def task_1_v1():
    soup = BeautifulSoup(xml_code, 'lxml')
    blue_cnt, red_cnt, green_cnt = [n for n in [0, 0, 0]]

    for cube in soup('cube', color='blue'):
        parent_cube = cube
        while parent_cube.name != 'body':
            parent_cube = parent_cube.parent
            blue_cnt += 1

    for cube in soup('cube', color='green'):
        parent_cube = cube
        while parent_cube.name != 'body':
            parent_cube = parent_cube.parent
            green_cnt += 1

    for cube in soup('cube', color='red'):
        parent_cube = cube
        while parent_cube.name != 'body':
            parent_cube = parent_cube.parent
            red_cnt += 1

    print(red_cnt, green_cnt, blue_cnt)


def task_1_v2():
    class MaxDepth:
        maxDepth = [0, 0, 0]
        depth = 0
        all_depth = [0, 0, 0]

        def start(self, tag, attrib):
            self.depth += 1
            if attrib['color'] == 'red':
                if self.depth > self.maxDepth[0]:
                    self.maxDepth[0] = self.depth
                self.all_depth[0] += self.depth

            if attrib['color'] == 'green':
                if self.depth > self.maxDepth[1]:
                    self.maxDepth[1] = self.depth
                self.all_depth[1] += self.depth

            if attrib['color'] == 'blue':
                if self.depth > self.maxDepth[2]:
                    self.maxDepth[2] = self.depth
                self.all_depth[2] += self.depth

        def end(self, tag):  # Called for each closing tag.
            self.depth -= 1

        def close(self):  # Called when all data has been parsed.
            return self.all_depth


    target = MaxDepth()
    parser = XMLParser(target=target)
    parser.feed(xml_code)
    res = parser.close()
    print(res[0], res[1], res[2])


if __name__ == '__main__':
    # task_1_v1()
    task_1_v2()