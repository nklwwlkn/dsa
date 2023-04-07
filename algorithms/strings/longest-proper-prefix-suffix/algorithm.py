# O(n) Time / O(n) Space

def longest_proper_prefix_suffix(pattern):
    lps = [0] * len(pattern)

    prefi = 0
    for i in range(1, len(pattern)):
        while prefi and pattern[i] != pattern[prefi]:
            prefi = lps[prefi - 1]

        if pattern[prefi] == pattern[i]:
            prefi += 1
            lps[i] = prefi

    return lps

# Test cases
test_cases = [
    ("ababab", [0,0,1,2,3,4]),
    ("level", [0,0,0,0,1]),
    ("bbbbbbz", [0,1,2,3,4,5,0]),
    ("abcdefg", [0, 0, 0, 0, 0, 0, 0]),
    ("a", [0]),
    ("", [])
]

# Run tests
for i, (input_arr, expected_output) in enumerate(test_cases):
    result = longest_proper_prefix_suffix(input_arr)
    assert result == expected_output, f"Test case {i} failed: expected {expected_output}, got {result}"
    print(f"Test case {i} passed")