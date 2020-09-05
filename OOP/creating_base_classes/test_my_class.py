from unittest import TestCase


class TestClasses(TestCase):
    """ Check before class structure change. """
    get_score_res = (2/3, 0.4, 2/3)
    get_answer_res = [1, 0, 1]

    def test_ClassA(self):
        from OOP.creating_base_classes.my_class import A
        class_a = A([2, 0, 1], [2, 0, 1])

        get_score_res = class_a.get_score()
        get_answer_res = class_a.get_answer()

        self.assertEqual(get_score_res, self.get_score_res[0])
        self.assertEqual(get_answer_res, self.get_answer_res)
        self.assertEqual(class_a.get_loss(), 0)

    def test_ClassB(self):
        from OOP.creating_base_classes.my_class import B
        class_b = B([2, 0, 1], [2, 0, 1])
        get_score_res = class_b.get_score()
        get_answer_res = class_b.get_answer()

        self.assertEqual(get_score_res, self.get_score_res[1])
        self.assertEqual(get_answer_res, self.get_answer_res)
        self.assertRaises(ValueError, class_b.get_loss)  # (!)

    def test_ClassC(self):
        from OOP.creating_base_classes.my_class import C
        class_c = C([2, 0, 1], [2, 0, 1])
        get_score_res = class_c.get_score()
        get_answer_res = class_c.get_answer()

        self.assertEqual(get_score_res, self.get_score_res[2])
        self.assertEqual(get_answer_res, self.get_answer_res)
        self.assertEqual(class_c.get_loss(), 0)