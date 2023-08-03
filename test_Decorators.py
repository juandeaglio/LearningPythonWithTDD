import os
import unittest
from tempfile import TemporaryFile


class Decorators(unittest.TestCase):
    def test_unDecoratedFunction(self):
        self.assertTrue("hello" == self.greet())

    def greet(self):
        return "hello"



if __name__ == '__main__':
    unittest.main()
