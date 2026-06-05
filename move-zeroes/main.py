test_cases = [
    {
        "name": "normal mixed case",
        "input": [0, 1, 0, 3, 12],
        "expected": [1, 3, 12, 0, 0],
    },
    {
        "name": "all zeroes",
        "input": [0, 0, 0],
        "expected": [0, 0, 0],
    },
    {
        "name": "no zeroes",
        "input": [1, 2, 3],
        "expected": [1, 2, 3],
    },
    {
        "name": "empty list",
        "input": [],
        "expected": [],
    },
    {
        "name": "single zero",
        "input": [0],
        "expected": [0],
    },
    {
        "name": "single non-zero",
        "input": [5],
        "expected": [5],
    },
    {
        "name": "zero at start",
        "input": [0, 1],
        "expected": [1, 0],
    },
    {
        "name": "zero at end",
        "input": [1, 0],
        "expected": [1, 0],
    },
    {
        "name": "multiple zeroes before number",
        "input": [0, 0, 1],
        "expected": [1, 0, 0],
    },
    {
        "name": "alternating zeroes",
        "input": [1, 0, 2, 0, 3],
        "expected": [1, 2, 3, 0, 0],
    },
    {
        "name": "negative numbers",
        "input": [0, -1, 0, 2, -3],
        "expected": [-1, 2, -3, 0, 0],
    },
    {
        "name": "many zeroes in middle",
        "input": [4, 0, 0, 0, 5],
        "expected": [4, 5, 0, 0, 0],
    },
]

# def move_zeroes(nums: list[int]) -> list[int]:
#     result = []
#     zeroes = []

#     for num in nums:
#         if num == 0:
#             zeroes.append(0)
#         else:
#             result.append(num)

#     return result + zeroes

def move_zeroes(nums: list[int]) -> list[int]:
    
    last_zero_index = -1

    for i in range(len(nums)):
        
        cur_num = nums[i]

        if cur_num == 0 and last_zero_index == -1:
            last_zero_index = i

        if cur_num != 0 and last_zero_index != -1:

            nums[last_zero_index] = cur_num
            nums[i] = 0
            last_zero_index += 1

    return nums

# nums = [0, 1, 0, 3, 12]
# print(move_zeroes(nums=nums))

for index, test in enumerate(test_cases, start=1):
    nums = test["input"].copy()
    result = move_zeroes(nums)

    if result == test["expected"]:
        print(f"Test {index} Passed: {test['name']}")
    else:
        print(f"Test {index} Failed: {test['name']}")
        print(f"  input:    {test['input']}")
        print(f"  expected: {test['expected']}")
        print(f"  got:      {result}")
        