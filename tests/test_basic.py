import unittest
import os
import sys
import io
# Import package in vscode
sys.path.append(os.path.dirname(os.path.dirname
                (os.path.abspath(__file__))))
from pylog import pylog
from tests import MODEL, TEST_VALUE, FULL_MODEL


class TestBasic(unittest.TestCase):

    @classmethod
    def tearDownClass(self):
        if os.path.exists(pylog.PyLog().path):
            os.remove(pylog.PyLog().path)

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
        sys.stdout = io.StringIO()
        log.logger(TEST_VALUE, MODEL[0], False)
        self.assertMultiLineEqual(str(sys.stdout.getvalue()), '')

    def test_wrong_attribute(self):
        with self.assertRaises(AttributeError):
            log = pylog.PyLog()
            log.logger(TEST_VALUE, "A")

    def test_clean(self):
        log = pylog.PyLog()
        log.logger(TEST_VALUE, MODEL[0])
        log.clean(False)
        self.assertFalse(os.path.exists(log.path))

    def test_FPylog(self):
        log = pylog.FPyLog()
        i = 0
        for _ in range(3):
            sys.stdout = io.StringIO()
            log.flogger(TEST_VALUE + "$f[cmd::]$" + TEST_VALUE, MODEL[i])
            output = str(sys.stdout.getvalue())
            part_out = output.split("\n")
            self.assertEqual(part_out[0].split(":")[-1], f"{TEST_VALUE}")
            # Test string can not include letter "m"
            self.assertEqual(part_out[0].split("\033[0m")[0]
                             .split("m")[-1], FULL_MODEL[i])

            self.assertEqual(part_out[2].split(":")[-1], f"{TEST_VALUE}")
            self.assertEqual(part_out[2].split("\033[0m")[0]
                             .split("m")[-1], FULL_MODEL[i])
            self.assertEqual(part_out[1], "0")
            i += 1

    def test_more_one_funtion(self):
        log = pylog.FPyLog()
        sys.stdout = io.StringIO()
        log.flogger(TEST_VALUE + "$f[cmd::]$$f[cmd::]$" + TEST_VALUE, MODEL[0])
        output = str(sys.stdout.getvalue())
        self.assertIs(output, '')

    def test_fprint(self):
        log = pylog.FPyLog()
        i = 0
        for _ in range(3):
            sys.stdout = io.StringIO()
            log.flogger(TEST_VALUE, MODEL[i])
            output = str(sys.stdout.getvalue())
            self.assertEqual(output.split(":")[-1], f"{TEST_VALUE}\n")

            # Test string can not include letter "m"
            self.assertEqual(output.split("\033[0m")[0]
                             .split("m")[-1], FULL_MODEL[i])
        
        i = 0
        for _ in range(3):
            sys.stdout = io.StringIO()
            log.flogger(TEST_VALUE + "\\$f[cmd]$", MODEL[i])
            output = str(sys.stdout.getvalue())
            self.assertEqual(len(output.split("\n")), 2)
            self.assertEqual(output.split(":")[-1],
                             f"{TEST_VALUE}\\$f[cmd]$\n")

            # Test string can not include letter "m"
            self.assertEqual(output.split("\033[0m")[0]
                             .split("m")[-1], FULL_MODEL[i])
