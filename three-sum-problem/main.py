def solve_three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()

    answer = []

    for i in range(len(nums)):
        """When we start looking at positive number, they can't add up to 0.
        So instead checking break the loop"""
        if nums[i] > 0:
            break

        """This condition is to avoid duplicate numbers that are already
        processed."""
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]

            if cur_sum == 0:
                answer.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                """This is again to skip the duplicate numbers from left side
                [-2, 0, 0, 0, 2, 2]"""
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                """Skip duplicate numbers from right side
                [-2, 0, 0, 0, 2, 2]"""
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif cur_sum < 0:
                left += 1

            else:
                right -= 1

    return answer


test_cases = [
    {
        "name": "leetcode sample with duplicates",
        "input": [-1, 0, 1, 2, -1, -4],
        "expected": [[-1, -1, 2], [-1, 0, 1]],
    },
    {
        "name": "all zeros collapse to one triplet",
        "input": [0, 0, 0, 0],
        "expected": [[0, 0, 0]],
    },
    {
        "name": "not enough numbers",
        "input": [0, 1],
        "expected": [],
    },
    {
        "name": "empty list",
        "input": [],
        "expected": [],
    },
    {
        "name": "no zero-sum triplet",
        "input": [1, 2, -2, -1],
        "expected": [],
    },
    {
        "name": "positive numbers only",
        "input": [1, 2, 3, 4, 5],
        "expected": [],
    },
    {
        "name": "negative numbers only",
        "input": [-5, -4, -3, -2, -1],
        "expected": [],
    },
    {
        "name": "multiple unique triplets",
        "input": [-4, -2, -2, -1, 0, 1, 2, 2, 3],
        "expected": [[-4, 1, 3], [-4, 2, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]],
    },
    {
        "name": "duplicates around valid pair",
        "input": [-2, 0, 0, 2, 2],
        "expected": [[-2, 0, 2]],
    },
    {
        "name": "sample mixed values",
        "input": [-2, -1, 0, 1, 2, 3],
        "expected": [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]],
    },
]


def normalize_triplets(triplets: list[list[int]]) -> list[list[int]]:
    return sorted([sorted(triplet) for triplet in triplets])


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
    result = solve_three_sum(nums=nums)
    actual = normalize_triplets(result)
    expected = normalize_triplets(test["expected"])
    passed_tests += print_test_result(
        index,
        test["name"],
        actual == expected,
        {
            "input": test["input"],
            "expected": expected,
            "got": actual,
        },
    )

print(f"Summary: {passed_tests}/{len(test_cases)} tests passed")
