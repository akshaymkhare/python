def find_missing_number(sequence):
    n = len(sequence) + 1
    expected_sum = (n * (n + 1)) // 2
    print("expected_sum:", expected_sum)
    actual_sum = sum(sequence)
    print("actual_sum:", actual_sum)
    missing_number = expected_sum - actual_sum
    return missing_number

# Example usage

sequence = list(range(1,10000000)) # [1, 2, 4, 5, 6]
sequence.remove(9992229)
missing_number = find_missing_number(sequence)
print("Missing number:", missing_number)