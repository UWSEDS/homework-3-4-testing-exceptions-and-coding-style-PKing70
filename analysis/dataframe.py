"""
This module loads a public dataset into a dataframe,
according to the instructions given for DATA 515 HW3.

The dataset loaded is Seattle Real Time Fire 911 calls from:
https://data.seattle.gov/Public-Safety/Seattle-Real-Time-Fire-911-Calls/kzjm-xkqj

As specified in the assignment:
https://github.com/UWSEDS/homework-3-4-testing-exceptions-and-coding-style-PKing70
"""
import pandas as pd

def read_dataframe():
    """
    Reads the data, as chosen from HW2.

    Args:
        None

    Returns:
        fire_df: A dataframe full of Seattle Real Time Fire 911 Call data.
    """
    fire_df = pd.read_csv('Seattle_Real_Time_Fire_911_Calls.csv', delimiter=',')
    return fire_df
