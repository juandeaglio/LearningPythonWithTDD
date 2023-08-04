import os
from tempfile import TemporaryFile


class TestContextManagers:
    def test_createTempFileWithinContext(self):
        with TemporaryFile() as f:
            assert os.path.exists(f.name)
        assert os.path.exists(f.name) is False
