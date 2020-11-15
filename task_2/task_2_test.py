import unittest

import task_2


class TestRoad(unittest.TestCase):

    def test_calc_weight_all_params_exist(self):
        road = task_2.Road(5000, 20)
        self.assertIsNone(road.calc_weight())

    def test_calc_weight_eq(self):
        road = task_2.Road(5000, 20)
        road.weight_square_meter = 25
        road.thickness = 0.05
        self.assertEqual(road.calc_weight(), 125000)


if __name__ == '__main__':
    unittest.main()
