# README.md

## Overview

This project focuses on calculating the **minimum number of comparisons** required for **Non-Dominated Sorting Fronts**, a critical operation in multi-objective optimization problems. Non-Dominated Sorting is essential for identifying the rank or "fronts" of solutions based on their dominance relationships.

The Python scripts in this project are used to generate all integer partitions of numbers from 2 to 100. These partitions are analyzed to determine the **optimal configurations** that minimize the number of comparisons required for sorting. These calculations significantly reduce the computational complexity of Non-Dominated Sorting algorithms, making them more efficient.

The code is organized into two separate Python files located in the `Code/` directory, and the generated CSV files are stored in the `csv/` directory.

This README explains how the code works, how partitions are generated, and how these computations contribute to achieving efficient Non-Dominated Sorting by minimizing the number of comparisons.

---

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Understanding Integer Partitions](#understanding-integer-partitions)
- [Code Structure](#code-structure)
  - [Generating Partitions](#generating-partitions)
  - [Calculating Comparisons](#calculating-comparisons)
- [Running the Code](#running-the-code)
- [Output Files](#output-files)
- [Interpreting the Results](#interpreting-the-results)
- [Conclusion](#conclusion)
- [Further Exploration](#further-exploration)
- [Contact Information](#contact-information)

---

## Introduction

In multi-objective optimization, Non-Dominated Sorting is used to divide solutions into "fronts" based on their dominance relationships. The goal is to assign each solution to a rank with minimal computational effort, measured by the number of comparisons needed.

This project applies integer partitions to optimize the sorting process. For a given number of solutions `n`, integer partitions represent possible groupings of solutions, and the number of comparisons required to sort them is analyzed. The optimal partition minimizes the total comparisons.

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

An integer partition divides a positive integer `n` into a set of positive integers that sum up to `n`. These partitions represent possible groupings of solutions in Non-Dominated Sorting, where each group corresponds to a level of dominance.

**Example for n = 5:**

- 5
- 4 + 1
- 3 + 2
- 3 + 1 + 1
- 2 + 2 + 1
- 2 + 1 + 1 + 1
- 1 + 1 + 1 + 1 + 1

Each partition defines how comparisons are distributed across groups. The total number of comparisons depends on the structure of the partition, and the goal is to find the partition that minimizes this total.

---

## Code Structure

### Generating Partitions

The function `generate_partitions(n)` is central to both scripts. It generates all unique partitions of a given integer `n` using recursion and backtracking.

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

### Calculating Comparisons

For each partition, the total number of comparisons is calculated as the sum of two terms:

1. **Combination Comparisons**:
   - Represents the number of comparisons within each group of `ni` elements in the partition.
   - **Formula**:
     ```
     comb_comparisons = sum((ni * (ni - 1)) / 2)
     ```
     where `ni` is each number in the partition.

2. **Positional Comparisons**:
   - Models the additional comparisons required based on the position of the group in the dominance hierarchy.
   - Calculated differently in each script:
     - **Binary Search Model**:
       - **Formula**:
         ```
         positional_comparisons = sum(ni * ceil(log2(i)))
         ```
         where `i` is the position of the group.
     - **Linear Model**:
       - **Formula**:
         ```
         positional_comparisons = sum(ni * (i - 1))
         ```

The total comparisons are then: 
total_comparisons = comb_comparisons + positional_comparisons

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

| n   | Min Comparisons | Partitions       |
|-----|-----------------|------------------|
| 4   | 6               | [[4], [2, 2]]    |

**Explanation**:

- **Minimum Comparisons**: 6
- **Optimal Partitions**:
  - `[4]`: Single group of 4 elements.
  - `[2, 2]`: Two groups, each with 2 elements.

### Observations

- Partitions with fewer, larger groups often reduce comparisons within groups but increase positional comparisons.
- The optimal partition balances these two factors to minimize total comparisons.

---

## Conclusion

This project demonstrates how integer partitions can be analyzed to minimize the number of comparisons required for Non-Dominated Sorting. By generating all possible partitions and calculating their comparison costs, we identify the optimal configurations for efficient sorting.

The results are directly applicable to improving the performance of Non-Dominated Sorting algorithms in multi-objective optimization.

---

## Further Exploration

- **Algorithm Optimization**: Use the results to optimize Non-Dominated Sorting algorithms.
- **Mathematical Analysis**: Investigate patterns in the optimal partitions across different `n`.
- **Comparison Models**: Explore alternative models for calculating comparisons.

---

## Contact Information

If you have any questions, suggestions, or would like to contribute to this project, please contact:

- **Name**: Jasteg Singh
- **Email**: jastegsingh007@gmail.com

We appreciate your interest and feedback!

