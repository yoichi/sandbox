"test"
import unittest


class TestFoo(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)
