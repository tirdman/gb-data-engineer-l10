import unittest

import task_1


class TestSalaryCalc(unittest.TestCase):

    def test_salary_val(self):
        self.assertEqual(task_1.salary_calc(48, 2000, 5000),
                         101000)

    def test_wrong_input(self):
        with self.assertRaises(ValueError):
            task_1.salary_calc(48, 2000, 't1')


if __name__ == '__main__':
    unittest.main()
