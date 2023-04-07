# Longest Proper Prefix Suffix Algorithm

The **Longest Proper Prefix Suffix (LPS)** algorithm is an efficient algorithm used to find the longest proper prefix which is also a suffix of a given string.

## How it works

The algorithm works by iterating over each character in the pattern string using a **for** loop, starting from index **1**. For each index **i**, the algorithm performs three phases:

1. At each iteration of the loop, the algorithm considers the substring pattern[0:i+1].

2. The algorithm checks if the current character **pattern[i]** matches the character at the position pointed to by the prefix pointer **prefi**. The prefix pointer **prefi** is initialized to **0** at the start and is incremented by **1** whenever a match is found. If a match is found, the length of the longest proper prefix that is also a suffix of the substring **pattern[0:i+1]** is recorded in the lps list at the current index **i**.

3. If there is no match, the prefix pointer is rolled back to the previous value **lps[prefi-1]**, and the algorithm continues to compare the current character **pattern[i]** with the character at the new position pointed to by the prefix pointer. This process is repeated until a match is found or the prefix pointer reaches **0**.

The algorithm terminates when all characters in the pattern string have been processed, and the final lps list is returned.

## Implementation

- [Python](./algorithm.py)

## Performance

The performance of the LPS algorithm is O(n) time and space, where n is the length of the pattern string. This is because the algorithm only iterates over the pattern string once and performs constant-time operations at each index.

## Applications

The LPS algorithm is useful in a variety of string matching and pattern recognition algorithms, such as the KMP (Knuth-Morris-Pratt) algorithm for finding occurrences of a pattern string in a text string. Specifically, the LPS values are used to determine where to continue the search in the text string when a mismatch occurs. The LPS algorithm can also be used in other applications, such as bioinformatics and natural language processing.