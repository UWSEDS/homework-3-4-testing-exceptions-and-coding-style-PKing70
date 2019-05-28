# Homework 3-4: Coding style and Unit tests.

See revisions based on initial grading, below.

##### Final grade: 14/14  


Grade: 11/14   

-1: df_test.py - line #45, if statement is redundant.    

-2: You have a lot of files in your working directory. This is fine, but you should have provided instructions regarding where everything is and how to use them.   


-------

**Note: This homework has a total of 14 points.**

In this homework, you will create two python modules and put them in PEP8 style.

1. Function code (5 points). Last week you wrote python codes that read an online file and created a data frame that has at least 3 columns. Now: (a) create a python module ``dataframe.py`` that reads the data in homework 2;  and (b) ``dataframpe.py`` should generate an ValueError execption if the dataframe doesn't have the expected column names.

1. Test code (5 points). Create a python file ``test_dataframe.py`` that has unit tests for dataframe.py. Include at least 2 of the following tests:

   - You have the expected columns.
   - Values in the column are all of the expected type.
   - There are no nan values.
   - The dataframe has at least one row.
   
1. Coding style (4 points). Make all codes PEP8 compliant and provide the output from pylint to demonstrate that you have accomplished this.

### Revisions based on grading

-1: df_test.py - line #45, if statement is redundant.

* Removed

-2: You have a lot of files in your working directory. This is fine, but you should have provided instructions regarding where everything is and how to use them.   

* I have reorganized the files to represent the structure requested in earlier homework:

'/analysis' contains my Python scripts for this assignment
'/data' contains my dataset for this assignment

### Instructions and Use

1. Clone this repo to your local working directory
2. From /analysis:

``dataframe.py`` contains a function to read the data from homework 2
``dataframpe.py`` contains a function to generate a ValueError exception if the dataframe doesn't have the expected columns

#### Dataframe.py (Question 1)

1. From /analysis, from the bash command line enter python:

```bash
$ python
```
2. From the Python command prompt, import ``dataframe.py``:
```python
>>> import dataframe as hwdf
```
3. From the Python command prompt, call ``read_dataframe()``:
```python
>>> hwdf.read_dataframe()
```
4. Expected output:
```python
                                        Address                        Type       ...                  Report Location  Incident Number
0                                           NaN                     --T::00       ...                              NaN              NaN
1                                6900 37th Av S              Medic Response       ...         (47.540683, -122.286131)       F110104166
2                       N 50th St / Stone Way N                Aid Response       ...         (47.665034, -122.340207)       F110104164
3                       E John St / E Olive Way                Aid Response       ...         (47.619575, -122.324257)       F110104165
4                                 611 12th Av S                Aid Response       ...         (47.597406, -122.317228)       F110104162
5                               4545 42nd Av Sw     Automatic Medical Alarm       ...         (47.562472, -122.385455)       F110104161
```

#### Dataframpe.py (Question 1)

Note that ``dataframpe.py`` imports and calls ``test_create_dataframe()`` from ``df_test.py``. You don't need to call ``test_create_dataframe()`` outside of ``dataframpe.py``.

1. From ``/analysis``, enter python:

```bash
$ python
```
2. From the Python command prompt, import ``dataframpe.py``:
```python
>>> import dataframpe as hwdfp
```
3. From the Python command prompt, call ``read_dataframe()``:
```python
>>> hwdf.read_dataframpe()
```
4. Expected output:
```python
                                        Address                        Type       ...                  Report Location  Incident Number
0                                           NaN                     --T::00       ...                              NaN              NaN
1                                6900 37th Av S              Medic Response       ...         (47.540683, -122.286131)       F110104166
2                       N 50th St / Stone Way N                Aid Response       ...         (47.665034, -122.340207)       F110104164
3                       E John St / E Olive Way                Aid Response       ...         (47.619575, -122.324257)       F110104165
4                                 611 12th Av S                Aid Response       ...         (47.597406, -122.317228)       F110104162
5                               4545 42nd Av Sw     Automatic Medical Alarm       ...         (47.562472, -122.385455)       F110104161
6                                   2124 3rd Av  Investigate Out Of Service       ...         (47.613347, -122.342498)       F110104160
7                             7605 Rainier Av S                Aid Response       ...         (47.534478, -122.269989)       F110104159
8                             2615 Sw Barton St              Medic Response       ...         (47.521023, -122.366095)       F110104158
9                               2028 Ne 65th St                Aid Response       ...         (47.675778, -122.305907)       F110104156...
```
5. To see the requested ValueError, go to line 30 of ``dataframpe.py`` and remove the comment so that it executes. 
```python
...
column_names.pop() #Uncomment this line to throw exception
...
```

This will make produce unexpected column names:
```python
>>> import dataframpe as hwdfp
>>> hwdfp.read_dataframpe()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/pking/Documents/GitHub/homework-3-4-testing-exceptions-and-coding-style-PKing70/analysis/dataframpe.py", line 32, in read_dataframpe
    if test_create_dataframe(fire_df, column_names, column_types, max_row_count):
  File "/Users/pking/Documents/GitHub/homework-3-4-testing-exceptions-and-coding-style-PKing70/analysis/df_test.py", line 44, in test_create_dataframe
    raise ValueError("DataFrame contains unexpected columns.")
ValueError: DataFrame contains unexpected columns.
```

#### Test_dataframe.py (Question 1)

Note that ``test_dataframe.py`` imports the ``unittest`` module and also imports ``read_dataframe()`` from ``dataframe.py``. You don't need to call ``read_dataframe()`` outside of ``test_dataframpe.py``.

1. From /analysis, from the command line, enter:

```bash
$ python test_dataframe.py
...
----------------------------------------------------------------------
Ran 3 tests in 5.919s

OK
```
You should see the expected output above, if all three tests pass.
