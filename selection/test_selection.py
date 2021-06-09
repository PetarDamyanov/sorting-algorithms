import unittest
from selection import selection


class TestSelection(unittest.TestCase):
    def test_selection(self):
        arr = [2, 5, 1, 3, 8, 6, 9]
        selection(arr)
        self.assertEqual(arr, [1, 2, 3, 5, 6, 8, 9])


if __name__ == '__main__':
    unittest.main()
