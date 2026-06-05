test_cases = [
    {
        "input": [1, 1],
        "expected": 1,
    },
    {
        "input": [2, 2],
        "expected": 2,
    },
    {
        "input": [2, 2, 2, 2],
        "expected": 6,
    },
    {
        "input": [1, 2, 3, 4, 5],
        "expected": 6,
    },
    {
        "input": [5, 4, 3, 2, 1],
        "expected": 6,
    },
    {
        "input": [1, 8, 6, 2, 5, 4, 8, 3, 7],
        "expected": 49,
    },
    {
        "input": [1, 100, 1, 1, 1, 100, 1],
        "expected": 400,
    },
    {
        "input": [0, 0],
        "expected": 0,
    },
    {
        "input": [100, 1, 1, 1, 1, 1, 100],
        "expected": 600,
    },
    {
        "input": [0, 2, 0, 2, 0],
        "expected": 4,
    },
]

"""First approach with out time complexity
"""
# def max_area(height: list[int]) -> int:

#     result = 0

#     for i in range(len(height)):

#         for j in range(i + 1, len(height)):

#             w = j - i
#             h = min(height[i], height[j])

#             if w * h > result:
#                 result = w * h

#     return result

"""More better approach considering the time complexity
not optimizing the solution
"""
# def max_area(height: list[int]) -> int:

#     result = 0

#     left = 0
#     right = len(height) - 1

#     for _ in range(len(height)):

#         w = right - left
#         h = min(height[left], height[right])

#         if w * h > result:
#             result = w * h

#         if height[left] > height[right]:
#             right -= 1
#         elif height[left] < height[right]:
#             left += 1
#         else:
#             right -= 1
#             left += 1
        
#     return result

"""Best approach and optimized for fatser speed
"""
def max_area(height: list[int]) -> int:

    result = 0

    left = 0
    right = len(height) - 1

    while left < right:

        w = right - left
        h = min(height[left], height[right])

        if w * h > result:
            result = w * h

        if height[left] > height[right]:
            right -= 1
        elif height[left] < height[right]:
            left += 1
        else:
            right -= 1
            left += 1
        
    return result

def print_test_result(index: int, name: str, passed: bool, details: dict[str, object]) -> int:
    status = "PASSED" if passed else "FAILED"
    print(f"Test {index}: {status} - {name}")

    if not passed:
        for label, value in details.items():
            print(f"  {label}: {value}")

    return int(passed)


passed_tests = 0

for index, test_case in enumerate(test_cases, start=1):
    actual = max_area(test_case["input"])
    passed_tests += print_test_result(
        index,
        f"case {index}",
        actual == test_case["expected"],
        {
            "input": test_case["input"],
            "expected": test_case["expected"],
            "got": actual,
        },
    )

print(f"Summary: {passed_tests}/{len(test_cases)} tests passed")
