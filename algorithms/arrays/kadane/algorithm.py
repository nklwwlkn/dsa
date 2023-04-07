# O(n) Time / O(1) Space

def kadane_algorithm(arr):
    max_sum = float('-inf')
    current_sum = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    
    return max_sum if max_sum != float('-inf') else 0

# Test cases
test_cases = [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1, 2, 3, 4, -10], 10),
    ([-2, -3, -4, -1, -2, -1, -5, -3], -1),
    ([1, -1, 1, -1, 1], 1),
    ([0, 0, 0, 0, 0], 0),
    ([], 0),
]

# Run tests
for i, (input_arr, expected_output) in enumerate(test_cases):
    result = kadane_algorithm(input_arr)
    assert result == expected_output, f"Test case {i} failed: expected {expected_output}, got {result}"
    print(f"Test case {i} passed")