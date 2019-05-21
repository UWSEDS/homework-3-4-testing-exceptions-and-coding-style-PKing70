"""
This module throws a value exception if the dataframe read by dataframe.py
does not have the expected column names, as specified for DATA 515 HW3.

As specified in the assignment:
https://github.com/UWSEDS/homework-3-4-testing-exceptions-and-coding-style-PKing70
"""
import pandas as pd

from df_test import test_create_dataframe

def read_dataframpe():
    """
    Reads the data, as chosen from HW2. Tests the data, using a version
    of df_test adapted from HW2 which now throws a value exception if the
    columns don't match what's expected.

    Args:
        None

    Returns:
        fire_df: A dataframe full of Seattle Real Time Fire 911 Call data, or None
        if the tests aren't passed.
    """
    fire_df = pd.read_csv('Seattle_Real_Time_Fire_911_Calls.csv', delimiter=',')
    column_names = fire_df.columns.values.tolist()
    column_types = fire_df.dtypes.tolist()
    max_row_count = 10

    #column_names.pop() #Uncomment this line to throw exception

    if test_create_dataframe(fire_df, column_names, column_types, max_row_count):
        return fire_df
    return None
