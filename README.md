# HW-01: Python, NumPy, and Pandas Foundations

## Objectives

The learning objectives of this assignment are to:

1. Build fluency in **core Python programming**, including variables, control structures, dictionaries, and list comprehensions.
2. Gain hands-on experience with **NumPy arrays**, including creation, indexing, broadcasting, and statistics.
3. Develop foundational skills with **Pandas Series and DataFrames** for loading, inspecting, cleaning, and aggregating data.
4. Practice writing **testable, modular Python code** that passes automated unit tests.
5. Follow professional **software quality standards** using automated linting.

---

## Setup Your Environment

Before starting, set up a Python environment. You will need the following tools and libraries:

* [Python (version 3.9 or higher)](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installation/)
* [numpy](https://numpy.org/)
* [pandas](https://pandas.pydata.org/)
* [pytest](https://docs.pytest.org/)
* [pylint](https://pylint.pycqa.org/)

---

### Installing Dependencies

Install the required dependencies with:

```bash
pip install -r requirements.txt
```

---

## Check Out the Starter Code

When you accepted the assignment, GitHub created a clone of the assignment
template for you at:

```
https://github.com/INFO-511-S25/python-numpy-pandas-hw-01-<your-username>
```

It also set up a separate `feedback` branch and a
[feedback pull request](https://docs.github.com/en/education/manage-coursework-with-github-classroom/teach-with-github-classroom/leave-feedback-with-pull-requests)
that will allow the instructional team to give you feedback on your work.

---

### Codespaces (Recommended)

**Codespaces are enabled.**

To launch a Codespace:

1. Click the green **Code** button
2. Select the **Codespaces** tab
3. Click **Create codespace on main**

This gives you a fully configured environment instantly.

---

### Local Machine (Alternative)

If you prefer working locally, clone the repository:

```bash
git clone https://github.com/INFO-511-S25/python-numpy-pandas-hw-01-<your-username>.git
cd python-numpy-pandas-hw-01-<your-username>
```

You are now ready to begin working on the assignment.
You should do all your work in the default branch, `main`.

---

## File Descriptions

### `ds.py`

This is the **only file you will modify**. It contains all required functions and variables for:

### ✅ Part 1: Python Basics

* `age`, `course`
* `get_age_and_course()`
* `is_prime(num)`
* `student_grades`
* `format_student_grades(...)`
* `compute_squares(numbers)`
* `filter_even_numbers(numbers)`

### ✅ Part 2: NumPy Foundations

* `create_example_arrays()`
* `array_properties(arr)`
* `array_arithmetic(x, y)`
* `slice_middle_row(arr)`
* `iterate_elements(arr)`
* `numpy_stats(arr)`

### ✅ Part 3: Pandas Foundations

* `create_example_series(data)`
* `create_example_dataframe()`
* `load_csv(path)`
* `inspect_dataframe(df)`
* `clean_dataframe(df)`
* `group_and_aggregate(df, group_col, value_col)`

Each function includes a **docstring explaining the expected behavior**.

---

### `test_ds.py`

This file contains the **automated tests** for your implementation.

* ✅ You **must not modify** this file.
* ✅ Your code will be graded entirely using this test file.
* ✅ Passing this file locally means your autograder will pass.

---

### `requirements.txt`

Lists the required Python packages for this assignment.

---

## Instructions

1. Open `ds.py` and **implement all functions and required variables**.
2. Follow the instructions in each function’s **docstring**.
3. Do **not** rename functions or modify function signatures.
4. Do **not** modify any other files.

---

## Running Tests

Run the full test suite with:

```bash
pytest
```

* Initially, the tests will fail because nothing is implemented.
* Once your code is correct, **all tests will pass**.

Example output when all tests pass:

```plaintext
============================= test session starts ==============================
collected 17 items

test_ds.py .................                             [100%]

============================== 17 passed in 0.08s ===============================
```

---

## Code Quality Checks (Required)

Run pylint to verify code style:

```bash
pylint ds.py
```

A perfect score looks like:

```plaintext
--------------------------------------------------------------------
Your code has been rated at 10.00/10
```

---

## Submission Instructions

1. Commit your changes to `ds.py`:

```bash
git add ds.py
git commit -m "Completed HW-01 Python, NumPy, and Pandas"
git push
```

2. **Do NOT:**

* Modify `test_ds.py`
* Modify `requirements.txt`
* Merge the feedback pull request

3. Verify your GitHub Actions checks are ✅ green.

---

## Grading

### ✅ Points Allocation

* **80 points** — All automated correctness (`pytest`) tests pass
* **10 points** — All automated code quality (`pylint`) checks pass
* **10 points** — Overall code quality:

  * Clear logic
  * Proper use of NumPy and Pandas
  * Clean function structure
  * Meaningful variable names
  * Appropriate use of Python control structures

---

### ❌ Deductions

You will lose **5 points each** for:

* Modifying any file other than `ds.py`
* Renaming required functions
* Editing or deleting docstrings
* Merging the `feedback` pull request
* Hardcoding values to pass specific test cases

---

✅ **This homework is foundational and will be relied on heavily in future assignments.**
Take the time to write clean, readable, testable code.

Good luck — and welcome to the Python data science pipeline! 🚀
