import unittest
from insert import insert


class TestInsert(unittest.TestCase):
    def test_insert(self):
        arr = [2, 5, 1, 3, 8, 6, 9]
        insert(arr)
        self.assertEqual(arr, [1, 2, 3, 5, 6, 8, 9])


if __name__ == '__main__':
    unittest.main()
