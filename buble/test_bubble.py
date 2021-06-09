import unittest
from bubble import bubble


class TestBubble(unittest.TestCase):
    def test_buble(self):
        arr = [2, 5, 1, 3, 8, 6, 9]
        bubble(arr)
        self.assertEqual(arr, [1, 2, 3, 5, 6, 8, 9])


if __name__ == '__main__':
    unittest.main()
