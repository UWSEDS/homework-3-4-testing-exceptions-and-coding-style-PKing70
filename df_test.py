"""
This module loads a public dataset into a dataframe, then tests the dataframe
according to the instructions given for DATA 515 HW2.

The dataset loaded is Seattle Real Time Fire 911 calls from:
https://data.seattle.gov/Public-Safety/Seattle-Real-Time-Fire-911-Calls/kzjm-xkqj

The tests are:
    The DataFrame contains only the columns that specified for the loaded data
    The columns contain the correct data type.
    There are at least 10 rows in the DataFrame

As specified in the assignment:
https://github.com/UWSEDS/hw2-using-functions-PKing70
"""

def test_create_dataframe(data, columns, types, rows_allowed):
    """
    Tests whether the data in a dataframe match the column name, data type,
    and row count constraints.

    Args:
        data (pandas.dataframe): Data loaded from a publicdata source (911 CSV
        from data.seattle.gov, in this case).

        columns(list): The header columns expected from the given data.

        types(list): The data types (after loading from CSV) from the given data.

        row_allowed(int): A row count that the dataframe must equal or surpass.
        In this case, 10 is tested.

    Returns:
        Boolean: Whether data passes all tests.

    Raises:
        ValueError: If the dataframe does not contain the same columns as the
        columns argument.
    """
    passed = sorted(data.columns.values.tolist()) == sorted(columns)
    if passed:
        passed = sorted(data.dtypes.tolist()) == sorted(types)
    else:
        raise ValueError("DataFrame contains unexpected columns.")
    if passed:
        passed = data.shape[0] >= rows_allowed
    return passed
