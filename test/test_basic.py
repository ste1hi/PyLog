import unittest
import os
import sys
import io
from pylog import pylog
from . import MODEL, TEST_VALUE, FULL_MODEL



class TestBasic(unittest.TestCase):
    
    def test_logfile_create(self):
        log = pylog.PyLog(False)
        for model in MODEL:
            log.logger(TEST_VALUE, model)
            self.assertTrue(os.path.exists(log.path))

    def test_print(self):
        log = pylog.PyLog()
        i = 0
        for _ in range(3):
            sys.stdout = io.StringIO()
            log.logger(TEST_VALUE, MODEL[i])
            output = str(sys.stdout.getvalue())
            self.assertEqual(output.split(":")[-1], f"{TEST_VALUE}\n")

            # Test string can not include letter "m"
            self.assertEqual(output.split("\033[0m")[0]
                             .split("m")[-1], FULL_MODEL[i])
            i += 1
