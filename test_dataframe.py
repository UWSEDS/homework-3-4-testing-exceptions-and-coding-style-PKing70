"""
This module tests the dataframe module using the unittest framework.
As specified in the assignment:
https://github.com/UWSEDS/homework-3-4-testing-exceptions-and-coding-style-PKing70
"""
import unittest
from dataframe import read_dataframe

class TestDataframe(unittest.TestCase):
    """TestDataframe unit tests the dataframe.py module function(s).

    Methods:
        test_expected_cols(self): Does the dataframe contain expected columns?
        test_no_nans(self): Are there any NaN values in the dataframe?
        test_one_row(self): Does the dataframe contain at least one row?
    """

    def test_expected_cols(self):
        """Asserts if columns in dataframe differ from what is known/expected.
        """
        expected_cols = ['Address', 'Type', 'Datetime', 'Latitude', \
            'Longitude', 'Report Location', 'Incident Number']
        read_cols = read_dataframe().columns.values.tolist()
        self.assertEqual(sorted(read_cols), sorted(expected_cols))

    def test_no_nans(self):
        """Asserts if there are any null values in the dataframe.
        """
        self.assertTrue(read_dataframe().isnull().values.any(), "There are NaNs!")

    def test_one_row(self):
        """Asserts if rows in not >= 1.
        """
        self.assertGreaterEqual(read_dataframe().shape[0], 1)

SUITE = unittest.TestLoader().loadTestsFromTestCase(TestDataframe)
_ = unittest.TextTestRunner().run(SUITE)
