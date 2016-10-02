import unittest

from binaryclassifier import __main__

class TestMain(unittest.TestCase):

    def test_transient_to_string(self):
        test_transient = ([(0.2, 1), (0.5, 3)], True)
        expected_output = "----------\n[(0.2, 1), (0.5, 3)]\nTrue\n"

        actual_output = __main__.transient_to_string(test_transient)

        self.assertEquals(expected_output, actual_output)
