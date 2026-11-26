"""
ds.py

Homework 1: Python, NumPy, and Pandas

Complete all questions by filling in the variables and functions below.
- Do not rename any existing variables or functions.
- You may add helper functions if needed, but do not change the public API.
- This file will be graded using pytest and pylint.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import statistics


# ============================================================
# Part 1: Python Basics
# ============================================================

# ------------------------------------------------------------
# Q1. Create two variables: an integer `age = 25` and a string
# `course = "Data Mining"`. Print both variables and their types.
# ------------------------------------------------------------

# TODO: assign these variables according to the question prompt.
age: int | None = None
course: str | None = None


def get_age_and_course() -> tuple[int, str]:
    """
    Return the age and course variables.

    This helper exists so that tests can easily check Q1 without
    depending on printed output.
    """
    if age is None or course is None:
        raise NotImplementedError(
            "Q1: You must assign values to `age` and `course`."
        )
    return age, course


# ------------------------------------------------------------
# Q2. Write a function `is_prime(num)` that uses control
# structures to determine whether a number is prime.
# ------------------------------------------------------------

def is_prime(num: int) -> bool:
    """
    Determine whether `num` is a prime number.

    Parameters
    ----------
    num : int
        The integer to test.

    Returns
    -------
    bool
        True if `num` is prime, False otherwise.

    TODO: Implement this function using control structures.
    """
    raise NotImplementedError("Q2: Implement is_prime(num).")


# ------------------------------------------------------------
# Q3. Create a dictionary `student_grades` with student names
# as keys and their grades as values. Then loop through the
# dictionary and print each student's name and grade in the
# format: `Student [Name] has grade [Grade]`.
# ------------------------------------------------------------

# TODO: populate this dictionary with a few example students.
student_grades: dict[str, float] = {}


def format_student_grades(
    grades: dict[str, float] | None = None,
) -> list[str]:
    """
    Return grade messages in the format:
    'Student [Name] has grade [Grade]'.

    This function is provided so tests can check your work
    without depending on printed output.

    Parameters
    ----------
    grades : dict[str, float] | None
        A dictionary of student names to grades. If None,
        the global `student_grades` is used.

    Returns
    -------
    list[str]
        A list of formatted strings.

    TODO: Implement this using a for-loop over the dictionary.
    """
    raise NotImplementedError("Q3: Implement format_student_grades().")


# ------------------------------------------------------------
# Q4. Use list comprehensions and define reusable functions.
# (Exact sub-tasks are intentionally open-ended here.)
# ------------------------------------------------------------

def compute_squares(numbers: list[int]) -> list[int]:
    """
    Return a list of squares for the given list of integers.

    This should be implemented using a list comprehension.

    Parameters
    ----------
    numbers : list[int]
        A list of integers.

    Returns
    -------
    list[int]
        A list containing n**2 for each n in `numbers`.

    TODO: Implement using a list comprehension.
    """
    raise NotImplementedError("Q4: Implement compute_squares().")


def filter_even_numbers(numbers: list[int]) -> list[int]:
    """
    Return a list containing only the even numbers from `numbers`.

    This should be implemented using a list comprehension.

    Parameters
    ----------
    numbers : list[int]
        A list of integers.

    Returns
    -------
    list[int]
        A list of even integers.

    TODO: Implement using a list comprehension.
    """
    raise NotImplementedError("Q4: Implement filter_even_numbers().")


# ============================================================
# Part 2: NumPy Introduction
# ============================================================

# ------------------------------------------------------------
# Q5. Create NumPy arrays and examine their properties.
# ------------------------------------------------------------

def create_example_arrays() -> dict[str, np.ndarray]:
    """
    Create example NumPy arrays and return them in a dictionary.

    Suggested:
    - a_1d: 1D array
    - a_2d: 2D array

    Returns
    -------
    dict[str, np.ndarray]
        A dictionary mapping names to arrays.

    TODO: Implement this function by creating at least one
    1D and one 2D NumPy array.
    """
    raise NotImplementedError("Q5: Implement create_example_arrays().")


def array_properties(arr: np.ndarray) -> dict[str, int]:
    """
    Return basic properties of a NumPy array: number of dimensions,
    shape, and size (total number of elements).

    Parameters
    ----------
    arr : np.ndarray
        Input array.

    Returns
    -------
    dict[str, int]
        A dictionary with keys 'ndim', 'shape_rows', 'shape_cols', 'size'.

    TODO: Implement this using `arr.ndim`, `arr.shape`, and `arr.size`.
    """
    raise NotImplementedError("Q5: Implement array_properties().")


# ------------------------------------------------------------
# Q6. Perform arithmetic and broadcasting with NumPy arrays.
# ------------------------------------------------------------

def array_arithmetic(x: np.ndarray, y: np.ndarray) -> dict[str, np.ndarray]:
    """
    Perform element-wise arithmetic between two arrays using broadcasting
    where appropriate.

    For example, you might compute:
    - sum_arr = x + y
    - diff_arr = x - y
    - prod_arr = x * y

    Parameters
    ----------
    x, y : np.ndarray
        Input arrays.

    Returns
    -------
    dict[str, np.ndarray]
        A dictionary of result arrays (e.g., 'sum', 'diff', 'prod').

    TODO: Implement this using NumPy arithmetic and broadcasting.
    """
    raise NotImplementedError("Q6: Implement array_arithmetic().")


# ------------------------------------------------------------
# Q7. Index, slice, and iterate over NumPy arrays.
# ------------------------------------------------------------

def slice_middle_row(arr: np.ndarray) -> np.ndarray:
    """
    Return the 'middle' row of a 2D NumPy array.

    For an array with shape (n_rows, n_cols), the middle row index
    can be taken as n_rows // 2.

    Parameters
    ----------
    arr : np.ndarray
        A 2D array.

    Returns
    -------
    np.ndarray
        The selected row as a 1D array.

    TODO: Implement this using NumPy indexing.
    """
    raise NotImplementedError("Q7: Implement slice_middle_row().")


def iterate_elements(arr: np.ndarray) -> list:
    """
    Iterate over all elements in the array and collect them
    into a Python list.

    Parameters
    ----------
    arr : np.ndarray

    Returns
    -------
    list
        A flat list of all elements in `arr`.

    TODO: Implement this using nested loops or `np.nditer`.
    """
    raise NotImplementedError("Q7: Implement iterate_elements().")


# ------------------------------------------------------------
# Q8. Calculate statistical metrics using NumPy.
# ------------------------------------------------------------

def numpy_stats(arr: np.ndarray) -> dict[str, float]:
    """
    Compute basic statistics of a 1D numeric NumPy array.

    Suggestion:
    - mean
    - median
    - standard deviation

    Parameters
    ----------
    arr : np.ndarray

    Returns
    -------
    dict[str, float]
        A dictionary with keys like 'mean', 'median', 'std'.

    TODO: Implement this using NumPy functions such as
    np.mean, np.median, np.std.
    """
    raise NotImplementedError("Q8: Implement numpy_stats().")


# ============================================================
# Part 3: Pandas Introduction
# ============================================================

# ------------------------------------------------------------
# Q9. Create and manipulate Series and DataFrames.
# ------------------------------------------------------------

def create_example_series(data: list[int] | list[float]) -> pd.Series:
    """
    Create a Pandas Series from a list of numeric data.

    Parameters
    ----------
    data : list[int] | list[float]

    Returns
    -------
    pd.Series

    TODO: Implement this using `pd.Series(data)`.
    """
    raise NotImplementedError("Q9: Implement create_example_series().")


def create_example_dataframe() -> pd.DataFrame:
    """
    Create a small example DataFrame, e.g. with columns like
    'name', 'age', and 'grade'.

    Returns
    -------
    pd.DataFrame

    TODO: Implement this using `pd.DataFrame({...})`.
    """
    raise NotImplementedError("Q9: Implement create_example_dataframe().")


# ------------------------------------------------------------
# Q10. Import and inspect CSV data using Pandas.
# ------------------------------------------------------------

def load_csv(path: str) -> pd.DataFrame:
    """
    Load a CSV file from `path` into a Pandas DataFrame.

    Parameters
    ----------
    path : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame

    TODO: Implement this using `pd.read_csv(path)`.
    """
    raise NotImplementedError("Q10: Implement load_csv().")


def inspect_dataframe(df: pd.DataFrame) -> dict[str, object]:
    """
    Inspect a DataFrame and return basic information such as:
    - number of rows
    - number of columns
    - column names

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    dict[str, object]
        E.g., {'n_rows': ..., 'n_cols': ..., 'columns': [...]}

    TODO: Implement this using `df.shape` and `df.columns`.
    """
    raise NotImplementedError("Q10: Implement inspect_dataframe().")


# ------------------------------------------------------------
# Q11. Clean and manipulate DataFrames (e.g., handle missing values).
# ------------------------------------------------------------

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic cleaning on a DataFrame.

    Suggested steps (you can adapt for your assignment spec):
    - Drop rows with all NaN values.
    - Optionally fill remaining NaNs with a default value or summary statistic.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
        A cleaned copy of the input DataFrame.

    TODO: Implement a simple cleaning strategy appropriate
    to your dataset/instructions.
    """
    raise NotImplementedError("Q11: Implement clean_dataframe().")


# ------------------------------------------------------------
# Q12. Group and aggregate data using Pandas.
# ------------------------------------------------------------

def group_and_aggregate(
    df: pd.DataFrame,
    group_col: str,
    value_col: str,
) -> pd.Series:
    """
    Group the DataFrame by `group_col` and compute the mean of `value_col`
    within each group.

    Parameters
    ----------
    df : pd.DataFrame
    group_col : str
        Column to group by.
    value_col : str
        Numeric column to aggregate.

    Returns
    -------
    pd.Series
        A series indexed by group with mean values.

    TODO: Implement this using `df.groupby(group_col)[value_col].mean()`.
    """
    raise NotImplementedError("Q12: Implement group_and_aggregate().")

