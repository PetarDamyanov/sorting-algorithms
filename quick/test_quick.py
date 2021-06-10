import unittest
from quick import quick


class TestQuick(unittest.TestCase):
    def test_quick(self):
        arr = [2, 5, 1, 3, 8, 6, 9]
        quick(0, len(arr) - 1, arr)
        self.assertEqual(arr, [1, 2, 3, 5, 6, 8, 9])


if __name__ == '__main__':
    unittest.main()
