import pandas as pd


# Function to generate all partitions of a number
def generate_partitions(n, max_num=None, current_partition=None, all_partitions=None):
    if current_partition is None:
        current_partition = []
    if all_partitions is None:
        all_partitions = []
    if max_num is None:
        max_num = n

    # Base case: If n is 0, add the current partition to the result
    if n == 0:
        all_partitions.append(current_partition[:])
        return all_partitions

    # Recursively generate partitions
    for i in range(min(max_num, n), 0, -1):
        current_partition.append(i)  # Choose a number
        generate_partitions(n - i, i, current_partition, all_partitions)
        current_partition.pop()  # Backtrack

    return all_partitions


# Function to calculate the minimum sum and related details for a given n
def find_min_sums_and_partitions(n):
    all_partitions = generate_partitions(n)
    min_sum = float('inf')
    min_partitions = []

    # Iterate through each partition
    for partition in all_partitions:
        comb_sum = 0
        prod_sum = 0

        for i, ni in enumerate(partition, start=1):
            # Calculate niC2 (combination sum)
            if ni >= 2:
                comb_sum += (ni * (ni - 1)) // 2

            # Calculate ni * (i - 1) (product sum)
            prod_sum += ni * (i - 1)

        # Calculate the total sum of the two sums
        total_sum = comb_sum + prod_sum

        # Update the minimum sum and its partitions
        if total_sum < min_sum:
            min_sum = total_sum
            min_partitions = [partition]
        elif total_sum == min_sum:
            min_partitions.append(partition)

    return min_sum, min_partitions


# Function to generate a table for a range of n values
def generate_min_sum_table(start, end):
    data = {"n": [], "Min Sum": [], "Partitions": []}

    for n in range(start, end + 1):
        print(n)
        min_sum, min_partitions = find_min_sums_and_partitions(n)
        data["n"].append(n)
        data["Min Sum"].append(min_sum)
        data["Partitions"].append(min_partitions)

    return pd.DataFrame(data)


# Main code to generate the table for n=2 to n=100
min_sum_table = generate_min_sum_table(2, 100)

# Save the table as a CSV file
file_path = "partition_table_with_min_sum.csv"
min_sum_table.to_csv(file_path, index=False)

print(f"Table saved successfully to: {file_path}"
