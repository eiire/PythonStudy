import unittest


class TestParse(unittest.TestCase):
    def test_parse(self):
        from _parser import parse

        test_cases = (
            ('wiki/Midline_nuclear_group', [2, 0, 3, 21]),
            ('wiki/Genus', [1, 3, 9, 19]),
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),
        )

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                res = parse(path)
                self.assertEqual(res[0], expected[0])
                self.assertEqual(res[1], expected[1])
                self.assertEqual(res[2], expected[2])
                self.assertEqual(res[3], expected[3])