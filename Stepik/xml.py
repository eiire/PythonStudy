from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

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


def tast_1_v2():
    pass


if __name__ == '__main__':
    # task_1_v1()
    task_1_v2()