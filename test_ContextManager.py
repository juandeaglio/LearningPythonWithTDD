import os
import unittest
from tempfile import TemporaryFile


class ContextManagers(unittest.TestCase):
    def test_createTempFileWithinContext(self):
        with TemporaryFile() as f:
            self.assertTrue(os.path.exists(f.name))
        self.assertFalse(os.path.exists(f.name))


if __name__ == '__main__':
    unittest.main()
