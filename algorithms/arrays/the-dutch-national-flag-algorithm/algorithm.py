
# O(n) Time / O(1) Space

def dutch_national_flag_algorithm(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

# Test cases
test_cases = [
    ([2, 1, 0, 2, 0, 1, 1, 0, 2, 1], [0, 0, 0, 1, 1, 1, 1, 2, 2, 2]),
    ([1, 2, 0, 2, 1, 0], [0, 0, 1, 1, 2, 2]),
    ([2, 2, 2], [2, 2, 2]),
    ([1, 1, 1], [1, 1, 1]),
    ([0, 0, 0], [0, 0, 0]),
    ([], []),
]

# Run tests
for i, (input_arr, expected_output) in enumerate(test_cases):
    result = dutch_national_flag_algorithm(input_arr)
    assert result == expected_output, f"Test case {i} failed: expected {expected_output}, got {result}"
    print(f"Test case {i} passed")