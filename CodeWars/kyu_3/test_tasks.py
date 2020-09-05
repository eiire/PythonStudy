from unittest import TestCase


class TestCalculator(TestCase):
    def test_evaluate(self):
        from CodeWars.kyu_3.tasks import Calculator
        res = list()
        res.append(Calculator().evaluate("1.1 + 2.2 + 3.3"))
        res.append(Calculator().evaluate("2 + 3 * 4 / 3 - 6 / 3 * 3 + 8"))
        self.assertEqual(res, [6.6, 8])
