# def remove_duplicate(nums: list[int]) -> int:
    
#     seen = []

#     for n in nums:
#         if n in seen:
#             pass
#         else:
#             seen.append(n)

#     return len(seen)

test_cases = [
    {
        "name": "empty list",
        "input": [],
        "expected_k": 0,
        "expected_nums": [],
    },
    {
        "name": "single element",
        "input": [1],
        "expected_k": 1,
        "expected_nums": [1],
    },
    {
        "name": "all unique",
        "input": [1, 2, 3, 4],
        "expected_k": 4,
        "expected_nums": [1, 2, 3, 4],
    },
    {
        "name": "all duplicates",
        "input": [2, 2, 2, 2],
        "expected_k": 1,
        "expected_nums": [2],
    },
    {
        "name": "duplicates in small sorted list",
        "input": [0, 0, 1, 1, 2],
        "expected_k": 3,
        "expected_nums": [0, 1, 2],
    },
    {
        "name": "leetcode sample",
        "input": [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        "expected_k": 5,
        "expected_nums": [0, 1, 2, 3, 4],
    },
    {
        "name": "negative numbers",
        "input": [-3, -3, -2, -1, -1, 0],
        "expected_k": 4,
        "expected_nums": [-3, -2, -1, 0],
    },
    {
        "name": "zero repeated between negatives and positives",
        "input": [-1, 0, 0, 0, 1],
        "expected_k": 3,
        "expected_nums": [-1, 0, 1],
    },
    {
        "name": "duplicates at the end",
        "input": [1, 2, 3, 3, 3],
        "expected_k": 3,
        "expected_nums": [1, 2, 3],
    },
    {
        "name": "large sorted values",
        "input": [100, 100, 1000, 1000, 10000],
        "expected_k": 3,
        "expected_nums": [100, 1000, 10000],
    },
]

def remove_duplicate(nums: list[int]) -> int:
    
    if len(nums) == 0:
        return 0
    
    last_index = 0

    for i in range(1, len(nums)):

        cur_num = nums[i]

        if cur_num != nums[last_index]:

            last_index += 1

            nums[last_index] = cur_num

    return last_index + 1


def print_test_result(index: int, name: str, passed: bool, details: dict[str, object]) -> int:
    status = "PASSED" if passed else "FAILED"
    print(f"Test {index}: {status} - {name}")

    if not passed:
        for label, value in details.items():
            print(f"  {label}: {value}")

    return int(passed)


passed_tests = 0

for index, test in enumerate(test_cases, start=1):
    nums = test["input"].copy()
    k = remove_duplicate(nums)
    unique_prefix = nums[:k]
    passed_tests += print_test_result(
        index,
        test["name"],
        k == test["expected_k"] and unique_prefix == test["expected_nums"],
        {
            "input": test["input"],
            "expected_k": test["expected_k"],
            "got_k": k,
            "expected_nums": test["expected_nums"],
            "got_nums": unique_prefix,
        },
    )

print(f"Summary: {passed_tests}/{len(test_cases)} tests passed")
