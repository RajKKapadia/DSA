# DSA Practice

This repository contains Python solutions for data structures and algorithms
practice problems. Each problem is self-contained in its own folder with a
`main.py` file.

## Problems

| Folder | Topics |
| --- | --- |
| `best-price-to-buy-sell-stock` | Arrays, one-pass minimum tracking |
| `container-with-most-water` | Arrays, two pointers |
| `linked-list` | Reversal, cycle detection, middle node, merging, removal, palindrome check |
| `move-zeroes` | Arrays, in-place two pointers |
| `remove-duplicated-sorted-array` | Sorted arrays, in-place two pointers |
| `three-sum-problem` | Sorting, two pointers, duplicate handling |
| `trapping-rain-water` | Arrays, prefix and suffix maximums |
| `two-sum` | Arrays, hash maps |
| `two-sum-sorted-array` | Sorted arrays, two pointers |

## Running a Solution

From the repository root, pass the problem folder to Python:

```bash
python3 two-sum/main.py
```

Alternatively, enter a problem folder and run its script directly:

```bash
cd two-sum
python3 main.py
```

Most scripts run inline test cases and print one result per case followed by a
summary:

```text
Test 1: PASSED - case 1
Summary: 15/15 tests passed
```

`trapping-rain-water/main.py` validates its cases with assertions, while
`linked-list/main.py` runs a direct palindrome-check example.
