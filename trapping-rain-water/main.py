# def calculate_trapping_water(height: list[int]) -> int:

#     total_water = 0

#     for i in range(1, len(height) - 1):
#         left_max = max(height[:i])
#         right_max = max(height[i + 1:])

#         cur_water = min(left_max, right_max) - height[i]

#         if cur_water > 0:
#             total_water += cur_water

#     return total_water


def calculate_trapping_water(height: list[int]) -> int:

    if len(height) < 3:
        return 0
    
    length = len(height)

    left_max = [0] * length
    left_max[0] = height[0]

    right_max = [0] * length
    right_max[length - 1] = height[length - 1]

    for i in range(1, length):
        left_max[i] = max(left_max[i - 1], height[i])

    for i in range(length - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    total_water = 0

    for i in range(1, len(height) - 1):

        cur_water = min(left_max[i], right_max[i]) - height[i]

        if cur_water > 0:
            total_water += cur_water

    return total_water


if __name__ == "__main__":
    test_cases = [
        # (input_list, expected_output, description)
        ([3, 0, 3], 3, "Simple V-shape"),
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6, "Standard LeetCode Example 1"),
        ([4, 2, 0, 3, 2, 5], 9, "Standard LeetCode Example 2"),
        ([], 0, "Empty list"),
        ([1], 0, "Single element"),
        ([1, 2], 0, "Two elements"),
        ([3, 3, 3, 3], 0, "Flat elevation"),
        ([1, 2, 3, 4, 5], 0, "Monotonically increasing"),
        ([5, 4, 3, 2, 1], 0, "Monotonically decreasing"),
        ([3, 1, 2, 1, 4], 5, "Multiple traps of different heights"),
        ([0, 0, 0, 0], 0, "All zeros")
    ]

    print("Running tests...")
    for i, (height, expected, desc) in enumerate(test_cases):
        result = calculate_trapping_water(height)
        assert result == expected, f"Test case {i} ({desc}) failed: expected {expected}, got {result}"
        print(f"Test case {i} ({desc}): Passed!")
    print("All tests passed successfully!")

