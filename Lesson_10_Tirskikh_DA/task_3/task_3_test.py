import unittest

import task_3


class TestRoad(unittest.TestCase):

    def test_add_return_valid_type(self):
        matrix_a = task_3.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        matrix_b = task_3.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertIsInstance(matrix_a + matrix_b, task_3.Matrix)

    def test_add_return_new_object(self):
        matrix_a = task_3.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        matrix_b = task_3.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertIsNot(matrix_a + matrix_b, matrix_a)


if __name__ == '__main__':
    unittest.main()
