import os
import unittest
from tempfile import TemporaryFile


class Decorators(unittest.TestCase):
    def test_decorateFunction(self):
        self.assertFalse(True)


if __name__ == '__main__':
    unittest.main()
