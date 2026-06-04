test_cases = [
    # 1. Basic sorted array
    {
        "nums": [2, 3, 4, 7, 11, 15],
        "target": 9,
        "expected": [0, 3],
    },

    # 2. Answer at beginning and end
    {
        "nums": [1, 2, 3, 4, 9],
        "target": 10,
        "expected": [0, 4],
    },

    # 3. Answer in the middle
    {
        "nums": [1, 2, 4, 6, 8, 11],
        "target": 10,
        "expected": [1, 4],  # 2 + 8
    },

    # 4. Negative numbers
    {
        "nums": [-10, -5, -2, 1, 4, 9],
        "target": -7,
        "expected": [1, 2],  # -5 + -2
    },

    # 5. Negative + positive
    {
        "nums": [-8, -3, 0, 2, 5, 11],
        "target": 3,
        "expected": [0, 5],  # -3 + 5
    },

    # 6. Zero involved
    {
        "nums": [-4, -1, 0, 3, 5],
        "target": 0,
        "expected": [],
    },

    # 7. Two zeros
    {
        "nums": [-3, 0, 0, 2, 5],
        "target": 0,
        "expected": [1, 2],
    },

    # 8. Duplicate numbers
    {
        "nums": [1, 2, 2, 3, 4],
        "target": 4,
        "expected": [0, 3],  # 1 + 3
    },

    # 9. Same number used twice, but two different indexes
    {
        "nums": [1, 3, 3, 5],
        "target": 6,
        "expected": [0, 3],
    },

    # 10. No pair exists
    {
        "nums": [1, 2, 4, 8, 16],
        "target": 15,
        "expected": [],
    },

    # 11. Empty array
    {
        "nums": [],
        "target": 5,
        "expected": [],
    },

    # 12. One element only
    {
        "nums": [5],
        "target": 10,
        "expected": [],
    },

    # 13. Two elements, valid
    {
        "nums": [4, 6],
        "target": 10,
        "expected": [0, 1],
    },

    # 14. Two elements, invalid
    {
        "nums": [4, 6],
        "target": 11,
        "expected": [],
    },

    # 15. Large numbers
    {
        "nums": [100, 500, 1000, 5000, 10000],
        "target": 15000,
        "expected": [3, 4],
    },
]

def two_sum(numbs: list[int], target: int) -> list[int]:

    left = 0
    right = len(numbs) - 1

    while left < right:

        cur_sum = numbs[left] + numbs[right]

        if cur_sum == target:
            return [left, right]
        elif cur_sum > target:
            right -= 1
        else:
            left += 1

    return []

# numbs = [2, 3, 4, 7, 11, 15]
# target = 9
# print(two_sum(numbs=numbs, target=target))

for index, test in enumerate(test_cases, start=1):
    result = two_sum(test["nums"], test["target"])

    if result == test["expected"]:
        print(f"Test {index}: Passed")
    else:
        print(f"Test {index}: Failed")
        print(f"  nums:     {test['nums']}")
        print(f"  target:   {test['target']}")
        print(f"  expected: {test['expected']}")
        print(f"  got:      {result}")
