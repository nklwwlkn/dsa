# Dutch National Flag Algorithm

The **Dutch National Flag Algorithm** is a sorting algorithm designed to efficiently partition an array of elements into three sections, based on a given pivot value. It was first proposed by Edsger Dijkstra, a Dutch computer scientist, and named after the Dutch flag, which has three horizontal stripes of red, white, and blue.

## How it works

The algorithm works by maintaining three pointers, which divide the array into four sections:

1. The first section contains elements less than the pivot value.
2. The second section contains elements equal to the pivot value.
3. The third section contains elements greater than the pivot value.
4. The fourth section contains unprocessed elements.

Initially, the first and second pointers point to the first element of the array, and the third pointer points to the last element of the array. The algorithm then iterates over the unprocessed elements, moving elements to their appropriate section by swapping them with the elements pointed to by the first and third pointers.

As the algorithm progresses, the first and second pointers move to the right, and the third pointer moves to the left, until all elements have been processed. At the end of the algorithm, the first and second sections contain all elements less than or equal to the pivot value, and the third section contains all elements greater than the pivot value.

## Implementation

- [Python](./algorithm.py)

## Performance

The Dutch National Flag Algorithm is commonly used in computer science to efficiently sort an array in linear time complexity, which is faster than traditional sorting algorithms such as bubble sort, insertion sort, or selection sort.

## Leetcode Problems:

1. [75. Sort Colors](https://leetcode.com/problems/sort-colors/description/)
