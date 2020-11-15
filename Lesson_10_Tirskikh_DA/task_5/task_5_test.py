import unittest

import task_5


class TestStorageEq(unittest.TestCase):

    def test_check_sn_duplicate_valid(self):
        storage = task_5.Storage('Склад 1')
        copier = task_5.Copier('white', 'xerox', '4490', 33333, ['A4', 'A3'])
        copier2 = task_5.Copier('white', 'xerox', '4490', 33334, ['A4'])
        copier3 = task_5.Copier('white', 'xerox', '4490', 33335, ['A4', 'A3'])
        copier4 = task_5.Copier('white', 'xerox', '4490', 33336, ['A4', 'A3', 'A2', 'A1'])
        storage.receive_equipment([copier, copier2, copier3, copier4])

        self.assertFalse(storage.check_sn_duplicate(copier4))

    def test_storage_list_have_real_objects(self):
        copier = task_5.Copier('white', 'xerox', '4490', 33333, ['A4', 'A3'])
        storage = task_5.Storage('Склад 1')
        storage.receive_equipment([copier])

        self.assertIs(copier, storage.storage_list.get(copier.type_eq())[0])

    def test_eq_diff_class(self):
        printer = task_5.Printer('black', 'samsung', '1210', 11111, True)
        self.assertNotIsInstance(printer, task_5.Copier)


if __name__ == '__main__':
    unittest.main()
