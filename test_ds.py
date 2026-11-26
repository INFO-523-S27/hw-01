"""
test_ds.py

Pytest-based autograding for ds.py (HW 1: Python, NumPy, and Pandas).

Assumes the following public API in ds.py:

- Variables:
    age, course, student_grades

- Functions:
    get_age_and_course
    is_prime
    format_student_grades
    compute_squares
    filter_even_numbers
    create_example_arrays
    array_properties
    array_arithmetic
    slice_middle_row
    iterate_elements
    numpy_stats
    create_example_series
    create_example_dataframe
    load_csv
    inspect_dataframe
    clean_dataframe
    group_and_aggregate
"""

import math
from typing import Any, Iterable

import numpy as np
import pandas as pd

import ds


# ---------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------


def almost_equal(a: float, b: float, tol: float = 1e-8) -> bool:
    """Numerical closeness helper."""
    return abs(a - b) <= tol


# ---------------------------------------------------------------------
# Q1. Basic variables
# ---------------------------------------------------------------------


def test_q1_age_and_course_values_and_types():
    assert hasattr(ds, "age"), "You must define a variable named `age`."
    assert hasattr(ds, "course"), "You must define a variable named `course`."

    assert isinstance(ds.age, int), "`age` should be an integer."
    assert ds.age == 25, "`age` should be exactly 25."

    assert isinstance(ds.course, str), "`course` should be a string."
    assert ds.course == "Data Mining", "`course` should be 'Data Mining'."


def test_q1_get_age_and_course_helper():
    """Helper should return the same values as the variables."""
    age, course = ds.get_age_and_course()
    assert age == ds.age
    assert course == ds.course


# ---------------------------------------------------------------------
# Q2. is_prime
# ---------------------------------------------------------------------


def test_q2_is_prime_basic_primes_and_composites():
    # Primes
    for p in [2, 3, 5, 7, 11, 13, 17, 19]:
        assert ds.is_prime(p), f"{p} should be prime."

    # Composites
    for c in [0, 1, 4, 6, 8, 9, 10, 12, 15, 20]:
        assert not ds.is_prime(c), f"{c} should NOT be prime."

    # Negative numbers should not be prime
    for n in [-1, -2, -5, -10]:
        assert not ds.is_prime(n), f"{n} should NOT be prime."


# ---------------------------------------------------------------------
# Q3. student_grades and format_student_grades
# ---------------------------------------------------------------------


def test_q3_student_grades_structure():
    assert hasattr(ds, "student_grades"), "You must define `student_grades`."
    grades = ds.student_grades

    assert isinstance(grades, dict), "`student_grades` must be a dict."
    assert len(grades) >= 2, "Include at least two students in `student_grades`."

    for name, grade in grades.items():
        assert isinstance(name, str), "All keys in `student_grades` must be strings."
        assert isinstance(
            grade, (int, float)
        ), "All values in `student_grades` must be numeric (int or float)."


def test_q3_format_student_grades_output_format_and_content():
    example_grades = {"Alice": 90, "Bob": 85}
    lines = ds.format_student_grades(example_grades)

    assert isinstance(lines, list), "format_student_grades should return a list."

    # We expect one formatted line per entry
    assert len(lines) == len(example_grades)

    for name, grade in example_grades.items():
        # Find strings that mention both the name and grade
        matching = [
            line for line in lines if name in line and str(grade) in line
        ]
        assert matching, f"No formatted line found for {name} with grade {grade}."

        for line in matching:
            assert line.startswith("Student "), "Line should start with 'Student '."
            assert (
                " has grade " in line
            ), "Line should contain the phrase ' has grade '."


# ---------------------------------------------------------------------
# Q4. List comprehensions
# ---------------------------------------------------------------------


def test_q4_compute_squares():
    numbers = [1, 2, 3, 4]
    expected = [1, 4, 9, 16]
    result = ds.compute_squares(numbers)
    assert result == expected, "compute_squares([1,2,3,4]) should return [1,4,9,16]."


def test_q4_filter_even_numbers():
    numbers = [1, 2, 3, 4, 5, 6]
    expected = [2, 4, 6]
    result = ds.filter_even_numbers(numbers)
    assert result == expected, "filter_even_numbers should keep only even numbers."


# ---------------------------------------------------------------------
# Q5. NumPy arrays and properties
# ---------------------------------------------------------------------


def test_q5_create_example_arrays_has_1d_and_2d():
    arrays = ds.create_example_arrays()
    assert isinstance(arrays, dict), "create_example_arrays must return a dict."

    assert "a_1d" in arrays, "Dictionary should contain key 'a_1d'."
    assert "a_2d" in arrays, "Dictionary should contain key 'a_2d'."

    a_1d = arrays["a_1d"]
    a_2d = arrays["a_2d"]

    assert isinstance(a_1d, np.ndarray)
    assert isinstance(a_2d, np.ndarray)

    assert a_1d.ndim == 1, "'a_1d' must be a 1D array."
    assert a_2d.ndim == 2, "'a_2d' must be a 2D array."
    assert a_1d.size > 0, "'a_1d' should not be empty."
    assert a_2d.size > 0, "'a_2d' should not be empty."


def test_q5_array_properties_correct_values():
    arr = np.arange(6).reshape(2, 3)
    props = ds.array_properties(arr)

    assert isinstance(props, dict), "array_properties must return a dict."
    for key in ("ndim", "shape_rows", "shape_cols", "size"):
        assert key in props, f"Key '{key}' missing from array_properties result."

    assert props["ndim"] == 2
    assert props["shape_rows"] == 2
    assert props["shape_cols"] == 3
    assert props["size"] == 6


# ---------------------------------------------------------------------
# Q6. Array arithmetic / broadcasting
# ---------------------------------------------------------------------


def test_q6_array_arithmetic_basic_ops():
    x = np.array([1, 2, 3])
    y = np.array([10, 20, 30])

    result = ds.array_arithmetic(x, y)

    assert isinstance(result, dict), "array_arithmetic must return a dict."
    for key in ("sum", "diff", "prod"):
        assert key in result, f"Key '{key}' missing from array_arithmetic result."

    np.testing.assert_array_equal(result["sum"], x + y)
    np.testing.assert_array_equal(result["diff"], x - y)
    np.testing.assert_array_equal(result["prod"], x * y)


# ---------------------------------------------------------------------
# Q7. Indexing, slicing, iterating over arrays
# ---------------------------------------------------------------------


def test_q7_slice_middle_row():
    arr = np.arange(12).reshape(4, 3)  # rows: 0,1,2,3
    expected = arr[4 // 2]  # row index 2
    middle = ds.slice_middle_row(arr)

    assert isinstance(middle, np.ndarray)
    np.testing.assert_array_equal(middle, expected)


def test_q7_iterate_elements_flattens_array():
    arr = np.array([[1, 2], [3, 4]])
    elems = ds.iterate_elements(arr)

    assert isinstance(elems, list), "iterate_elements should return a list."
    assert elems == [1, 2, 3, 4], "Elements should be returned in row-major order."


# ---------------------------------------------------------------------
# Q8. NumPy statistics
# ---------------------------------------------------------------------


def test_q8_numpy_stats_basic():
    arr = np.array([1.0, 2.0, 3.0, 4.0])
    stats = ds.numpy_stats(arr)

    for key in ("mean", "median", "std"):
        assert key in stats, f"Key '{key}' missing from numpy_stats result."

    assert almost_equal(stats["mean"], np.mean(arr))
    assert almost_equal(stats["median"], np.median(arr))
    assert almost_equal(stats["std"], np.std(arr))


# ---------------------------------------------------------------------
# Q9. Pandas Series and DataFrames
# ---------------------------------------------------------------------


def test_q9_create_example_series():
    data = [10, 20, 30]
    s = ds.create_example_series(data)

    assert isinstance(s, pd.Series), "create_example_series must return a Series."
    assert list(s.values) == data, "Series values should match the input list."


def test_q9_create_example_dataframe_structure():
    df = ds.create_example_dataframe()
    assert isinstance(df, pd.DataFrame), "create_example_dataframe must return a DataFrame."
    assert not df.empty, "Example DataFrame should not be empty."

    # Expect at least these three columns
    for col in ("name", "age", "grade"):
        assert col in df.columns, f"'{col}' column missing from example DataFrame."


# ---------------------------------------------------------------------
# Q10. CSV import and inspection
# ---------------------------------------------------------------------


def test_q10_load_csv_and_inspect_dataframe(tmp_path):
    # Create a temporary CSV file
    csv_path = tmp_path / "sample.csv"
    original_df = pd.DataFrame(
        {
            "name": ["Alice", "Bob"],
            "score": [95, 88],
        }
    )
    original_df.to_csv(csv_path, index=False)

    # Test load_csv
    loaded_df = ds.load_csv(str(csv_path))
    assert isinstance(loaded_df, pd.DataFrame)
    pd.testing.assert_frame_equal(loaded_df, original_df)

    # Test inspect_dataframe
    info = ds.inspect_dataframe(loaded_df)
    assert isinstance(info, dict)

    assert info.get("n_rows") == 2
    assert info.get("n_cols") == 2

    cols = info.get("columns")
    assert isinstance(cols, (list, pd.Index))
    assert set(cols) == {"name", "score"}


# ---------------------------------------------------------------------
# Q11. Cleaning DataFrames
# ---------------------------------------------------------------------


def test_q11_clean_dataframe_drops_all_nan_rows():
    df = pd.DataFrame(
        {
            "a": [1, np.nan, 3],
            "b": [4, np.nan, 6],
        }
    )
    # Make row 1 all NaN for both columns
    df.loc[1, :] = np.nan

    cleaned = ds.clean_dataframe(df)
    assert isinstance(cleaned, pd.DataFrame)

    # Row with all-NaN values should be removed
    assert len(cleaned) == 2, "clean_dataframe should drop rows with all NaNs."

    # Original non-NaN rows should still be present (by values)
    assert {1, 3} == set(cleaned["a"].dropna())
    assert {4, 6} == set(cleaned["b"].dropna())


# ---------------------------------------------------------------------
# Q12. Grouping and aggregation
# ---------------------------------------------------------------------


def test_q12_group_and_aggregate_mean():
    df = pd.DataFrame(
        {
            "group": ["A", "A", "B", "B"],
            "value": [10, 20, 5, 15],
        }
    )

    result = ds.group_and_aggregate(df, "group", "value")

    assert isinstance(result, pd.Series), "group_and_aggregate must return a Series."
    assert set(result.index) == {"A", "B"}

    # Means: A -> (10 + 20)/2 = 15; B -> (5 + 15)/2 = 10
    assert almost_equal(result["A"], 15.0)
    assert almost_equal(result["B"], 10.0)
