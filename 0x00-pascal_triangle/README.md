# Pascal's Triangle

This project implements Pascal's Triangle in Python, generating a list of lists representing the triangle up to a specified number of rows.

## Table of Contents

- [Introduction](#introduction)
- [Task](#task)
- [Directory Structure](#directory-structure)
- [How to Use](#how-to-use)
- [Testing](#testing)
- [Author](#author)
- [License](#license)

## Introduction

This project provides a Python implementation of Pascal's Triangle. Pascal's Triangle is a mathematical construct where each number is the sum of the two directly above it. The triangle starts with a single 1 and expands according to this rule.

## Task

The main task of this project is to create a function `pascal_triangle(n)` that returns a list of lists of integers representing Pascal’s Triangle of `n`. The function should return an empty list if `n` is less than or equal to 0.

The provided test script, `0-main.py`, demonstrates the function's usage and expected output.

## Directory Structure
* 0x00-pascal_triangle/
│
├── 0-pascal_triangle.py
├── 0-main.py
└── README.md


- `0-pascal_triangle.py`: Contains the implementation of the `pascal_triangle` function.
- `0-main.py`: Test script to verify the correctness of the `pascal_triangle` function.
- `README.md`: Project documentation.

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/Official0mega/alx-interview.git
   ```
2. cd alx-interview/0x00-pascal_triangle

3. ./0-main.py

- [x] This will execute the pascal_triangle function and print the generated Pascal's Triangle for a given input.

# Testing
* The project includes a test script, 0-main.py, which you can run to verify the correctness of your pascal_triangle function. The script will display the Pascal's Triangle for a specific input.
+ ./0-main.py

# Author
* Official0mega

# License
* This project is licensed under the MIT License - see the LICENSE file for details.



