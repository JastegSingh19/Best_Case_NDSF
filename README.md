# README.md

## Overview

This project focuses on calculating the minimum number of dominance comparisons required by the Efficient Non-dominated Sort Approach (Sequential and Binary versions) for the non-dominated sorting problem. The sequential version is known as **ENS-SS**, and the binary version is known as **ENS-BS**. Non-Dominated Sorting is important for identifying the rank of the solutions.

The Python scripts in this project are used to find the cardinality of the fronts that minimizes the number of dominance comparisons for both ENS-SS and ENS-BS. To find the cardinality of the front that minimizes the number of dominance comparisons, we explore all the possible cardinalities of the front for a population size and select the one that gives the minimum number of dominance comparisons. For exploring all the possible cardinalities of the fronts, we have used the concept of integer partitions and generated all the partitions (in non-increasing order). These partitions correspond to the cardinality of the fronts. We have considered the population size from 2 to 100 and obtained the cardinality of the fronts that minimize the number of dominance comparisons for ENS-SS and ENS-BS both.

The code is organized into two separate Python files located in the `Code/` directory, and the generated CSV files are stored in the `csv/` directory.

This README explains how the code works, how partitions are generated, and how these computations contribute to achieving the cardinality of the fronts.


---

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Understanding Integer Partitions](#understanding-integer-partitions)
- [Code Structure](#code-structure)
  - [Generating Partitions](#generating-partitions)
- [Running the Code](#running-the-code)
- [Output Files](#output-files)
- [Interpreting the Results](#interpreting-the-results)
- [Conclusion](#conclusion)
- [Contact Information](#contact-information)

---

## Introduction

In Pareto dominance-based multi-objective evolutionary algorithms, Non-Dominated Sorting is used to divide the solutions into "fronts" based on their dominance relationships. The goal is to assign each solution to a rank. This project applies the concept of integer partitions to find the cardinality of the front that minimizes the number of dominance comparisons by two approaches — **ENS-SS** and **ENS-BS**. For a given number of solutions `n`, integer partitions represent possible groupings of the solutions, and the number of dominance comparisons required to sort them is analyzed.


---

## Project Structure

The project directories are organized as follows:

- **`Code/`**: Contains the Python scripts.
  - `partition_with_min_comparisons_binary_search.py`: Calculates the number of comparisons using a binary search model.
  - `partition_with_min_comparisons_linear.py`: Calculates the number of comparisons using a linear model.
- **`csv/`**: Contains the generated CSV files.
  - `partition_table_with_min_comparisons_binary_search.csv`: Output from `partition_with_min_comparisons_binary_search.py`.
  - `partition_table_with_min_comparisons_linear.csv`: Output from `partition_with_min_comparisons_linear.py`.

Each script generates a CSV file that lists the minimum comparisons and the partitions that achieve them for each integer `n` from 2 to 100.

---

## Prerequisites

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **Pandas Library**: Used for handling data frames and CSV files.
  - Install via pip if not already installed:
    ```bash
    pip install pandas
    ```

---

## Understanding Integer Partitions


An integer partition divides a positive integer `n` into a set of positive integers that sum up to `n`. These partitions represent possible groupings of the solutions. For example, for `n = 5`, we have a partition `3 + 1 + 1`. It means the first front has 3 solutions, and the second and third fronts have one solution each — i.e., the cardinality of the first front is 3, and the cardinality of the second and third fronts is 1.

**Example for n = 5:**

- 5  
- 4 + 1  
- 3 + 2  
- 3 + 1 + 1  
- 2 + 2 + 1  
- 2 + 1 + 1 + 1  
- 1 + 1 + 1 + 1 + 1


---

## Code Structure

### Generating Partitions

The function `generate_partitions(n)` is central to both scripts. It generates all unique partitions of a given integer `n` using recursion and backtracking in non-increasing order, i.e., the elements of the partitions are generated in non-increasing order.


#### How It Works

1. **Initialization**:
   - **Parameters**:
     - `n`: The integer to partition.
     - `max_num`: The maximum number allowed in the current position (defaults to `n`).
     - `current_partition`: The current partition being built (initially empty).
     - `all_partitions`: A list to store all valid partitions (initially empty).
   - **Purpose**: Starts the recursive process to build partitions.

2. **Base Case**:
   - If `n` equals 0:
     - The `current_partition` is a valid partition.
     - Append a copy of `current_partition` to `all_partitions`.
     - Return `all_partitions`.

3. **Recursive Case**:
   - Iterate from `min(max_num, n)` down to 1:
     - Append `i` to `current_partition`.
     - Recursively call `generate_partitions(n - i, i, current_partition, all_partitions)` to continue partitioning the remaining sum.
     - Backtrack by removing `i` from `current_partition`.

This method ensures that partitions are generated in non-increasing order, avoiding duplicates due to different orders of the same numbers.

---

## Running the Code

1. Navigate to the `Code/` directory and run the scripts:
    ```bash
    python partition_with_min_comparisons_binary_search.py
    python partition_with_min_comparisons_linear.py
    ```

2. CSV files will be generated in the `csv/` directory.

---

## Output Files

- **`partition_table_with_min_comparisons_binary_search.csv`**
- **`partition_table_with_min_comparisons_linear.csv`**

---

## Interpreting the Results

Each row in the CSV files provides insights into the partitions that minimize the total comparisons for a given integer `n`.

### Example Entry

For `n = 4` in `partition_table_with_min_comparisons_binary_search.csv`:

| n   | Min Comparisons | Partitions                  |
|-----|-----------------|-----------------------------|
| 4   | 4               | [[3, 1], [2, 2], [2, 1, 1]] |

**Explanation**:

- **Minimum Comparisons**: 4  
- **Optimal Partitions**:
  - `[3, 1]`: One front with 3 solutions, another with 1.  
  - `[2, 2]`: Two fronts, each with 2 solutions.  
  - `[2, 1, 1]`: Three fronts, with sizes 2, 1, and 1.  


### Observations

- Partitions with fewer, larger groups often reduce comparisons within groups but increase positional comparisons.
- The optimal partition balances these two factors to minimize total comparisons.

---

## Conclusion

This project demonstrates how integer partitions can be linked to the cardinality of the fronts to find the best case scenario for an algorithm. By generating all possible partitions and calculating corresponding dominance comparisons, we identify the optimal configurations for ENS-SS and ENS-BS.

---

## Contact Information

If you have any questions, suggestions, or would like to contribute to this project, please contact:

- **Name**: Jasteg Singh
- **Email**: jastegsingh007@gmail.com

We appreciate your interest and feedback!

