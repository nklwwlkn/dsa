# Kadane's Algorithm
Kadane's Algorithm is a well-known algorithm used to find the maximum subarray sum of a given array of integers. A subarray is a contiguous subset of the array. The algorithm works by iterating over the array and keeping track of the maximum subarray sum found so far.

## How it works
1. Initialize two variables: max_sum and current_sum to zero or negative infinity.
2. Loop through each element of the array:
    - Add the current element to current_sum
    - If current_sum is greater than max_sum, update max_sum.
    - If current_sum becomes negative, reset it to zero.
3. Return max_sum.

## Implementation

- [Python](./algorithm.py)

## Performance

The time complexity of Kadane's Algorithm is O(n), where n is the length of the array. This is because the algorithm loops through the array only once, performing constant-time operations for each element. Therefore, Kadane's Algorithm is considered to be an efficient solution for finding the maximum subarray sum.

## Leetcode Problems:

1. [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)