import unittest
from merge import merge


class TestMerge(unittest.TestCase):
    def test_merge(self):
        arr = [2, 5, 1, 3, 8, 6, 9]
        merge(arr)
        self.assertEqual(arr, [1, 2, 3, 5, 6, 8, 9])


if __name__ == '__main__':
    unittest.main()
