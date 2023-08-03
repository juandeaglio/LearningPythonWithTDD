import os
import unittest
from tempfile import TemporaryFile


def say_goodbye():
    return "Goodbye"

class Decorators(unittest.TestCase):
    def test_unDecoratedFunction(self):
        self.assertTrue("Hello" == self.greet())

    def greet(self):
        return "Hello"

    def test_decoratedFunction(self):
        self.assertTrue("""Hello
Goodbye""" == self.conversation(self.greet))


    def conversation(self, introduction):
        return introduction() + "\n" + say_goodbye()



if __name__ == '__main__':
    unittest.main()
