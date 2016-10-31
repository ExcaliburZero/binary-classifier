import unittest

from binaryclassifier import __main__

class TestMain(unittest.TestCase):

    def test_transient_to_string(self):
        # Transient
        test_transient = ([(0.2, 1), (0.5, 3)], True)
        expected_output = "----------\n[(0.2, 1), (0.5, 3)]\nTransient: Success\n"
        actual_output = __main__.transient_to_string(True, test_transient)
        self.assertEquals(expected_output, actual_output)

        test_transient2 = ([(0.2, 1), (0.5, 3)], False)
        expected_output = "----------\n[(0.2, 1), (0.5, 3)]\nTransient: Failure\n"
        actual_output = __main__.transient_to_string(True, test_transient2)
        self.assertEquals(expected_output, actual_output)

        # Non-Transient
        test_non_transient = ([(0.2, 1), (0.5, 3)], False)
        expected_output3 = "----------\n[(0.2, 1), (0.5, 3)]\nNon-Transient: Success\n"
        actual_output3 = __main__.transient_to_string(False, test_non_transient)
        self.assertEquals(expected_output3, actual_output3)

        test_non_transient2 = ([(0.2, 1), (0.5, 3)], True)
        expected_output4 = "----------\n[(0.2, 1), (0.5, 3)]\nNon-Transient: Failure\n"
        actual_output4 = __main__.transient_to_string(False, test_non_transient2)
        self.assertEquals(expected_output4, actual_output4)
