test_cases = [
    # 1. Basic case
    {
        "nums": [2, 7, 11, 15],
        "target": 9,
        "expected": [0, 1],
    },

    # 2. Unsorted array
    {
        "nums": [3, 2, 4],
        "target": 6,
        "expected": [1, 2],
    },

    # 3. Repeated numbers
    {
        "nums": [3, 3],
        "target": 6,
        "expected": [0, 1],
    },

    # 4. Negative numbers
    {
        "nums": [-1, -2, -3, -4, -5],
        "target": -8,
        "expected": [2, 4],  # -3 + -5
    },

    # 5. One positive and one negative
    {
        "nums": [-3, 4, 3, 90],
        "target": 0,
        "expected": [0, 2],  # -3 + 3
    },

    # 6. Zero involved
    {
        "nums": [0, 4, 3, 0],
        "target": 0,
        "expected": [0, 3],
    },

    # 7. Duplicate values, but answer uses later duplicate
    {
        "nums": [1, 5, 5, 3],
        "target": 10,
        "expected": [1, 2],
    },

    # 8. Same value appears many times
    {
        "nums": [2, 2, 2, 2],
        "target": 4,
        "expected": [0, 1],
    },

    # 9. Answer at the end
    {
        "nums": [10, 20, 30, 40, 50],
        "target": 90,
        "expected": [3, 4],
    },

    # 10. Answer at first and last index
    {
        "nums": [8, 1, 2, 3, 7],
        "target": 15,
        "expected": [0, 4],
    },

    # 11. No valid pair
    {
        "nums": [1, 2, 3],
        "target": 7,
        "expected": [],
    },

    # 12. Empty array
    {
        "nums": [],
        "target": 5,
        "expected": [],
    },

    # 13. Only one element
    {
        "nums": [5],
        "target": 10,
        "expected": [],
    },

    # 14. Large numbers
    {
        "nums": [1000000, 5000000, -2000000, 7000000],
        "target": 3000000,
        "expected": [1, 2],  # 5000000 + -2000000
    },

    # 15. Multiple valid answers possible
    {
        "nums": [1, 2, 3, 4, 5],
        "target": 6,
        "expected": [1, 3],  # Your code returns 2 + 4, not 1 + 5
    },
]

# def two_sum(nums: list[int], target: int) -> list[int]:

#     for i in range(len(nums)):

#         for j in range(i + 1, len(nums)):

#             if nums[i] + nums[j] == target:
#                 return [i, j]

#     return 0

def two_sum(nums: list[int], target: int) -> list[int]:

    seen: dict[int, int] = {}

    for i in range(len(nums)):

        cur_num = nums[i]

        needed = target - cur_num

        if needed in seen:
            return [seen[needed], i]
        else:
            seen[cur_num] = i

    return []



# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums=nums, target=target))

def print_test_result(index: int, name: str, passed: bool, details: dict[str, object]) -> int:
    status = "PASSED" if passed else "FAILED"
    print(f"Test {index}: {status} - {name}")

    if not passed:
        for label, value in details.items():
            print(f"  {label}: {value}")

    return int(passed)


passed_tests = 0

for index, test in enumerate(test_cases, start=1):
    result = two_sum(test["nums"], test["target"])
    passed_tests += print_test_result(
        index,
        f"case {index}",
        result == test["expected"],
        {
            "nums": test["nums"],
            "target": test["target"],
            "expected": test["expected"],
            "got": result,
        },
    )

print(f"Summary: {passed_tests}/{len(test_cases)} tests passed")
