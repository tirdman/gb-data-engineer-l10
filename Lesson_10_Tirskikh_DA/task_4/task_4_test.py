import unittest

import task_4


class TestClothes(unittest.TestCase):

    def test_clothes_list_success_add(self):
        coat = task_4.Clothes('coat', 52)
        self.assertTrue(len(task_4.Clothes.clothe_items) > 0)

    def test_is_valid_clothe_type(self):
        coat = task_4.Clothes('coat', 52)
        self.assertIn(coat.close_type, task_4.clothe_types)

    def test_check_sn_duplicate_valid(self):
        coat = task_4.Clothes('coat', 52)
        self.assertIsNotNone(coat.get_clothes_rate)

    def test_get_clothes_rate_not_eq_diff_type(self):
        coat = task_4.Clothes('coat', 52)
        suite = task_4.Clothes('suite', 52)
        self.assertNotEqual(coat.get_clothes_rate, suite.get_clothes_rate)


if __name__ == '__main__':
    unittest.main()
