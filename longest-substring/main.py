# def find_longest_substring(s: str) -> int:
    
#     best = 0

#     for i in range(len(s)):

#         cur_longest = s[i]

#         for j in range(i + 1, len(s)):

#             if s[j] not in cur_longest:
#                 cur_longest += s[j]
#             else:
#                 break
        
#         if len(cur_longest) > best:
#             best = len(cur_longest)
            
#     return best


# def find_longest_substring(s: str) -> int:

#     if len(s) == 0:
#         return 0
    
#     left = 0
#     seen = set()

#     best = 0

#     for right in range(len(s)):

#         cur_char = s[right]

#         if cur_char not in seen:
#             seen.add(cur_char)

#         else:
#             while cur_char in seen:
#                 seen.remove(s[left])
#                 left += 1
            
#             seen.add(cur_char)

#         cur_length = right - left + 1

#         best = max(cur_length, best)
            
#     return best


test_cases = [
    {
        "name": "standard repeated pattern",
        "input": "abcabcbb",
        "expected": 3,
    },
    {
        "name": "all characters repeated",
        "input": "bbbbb",
        "expected": 1,
    },
    {
        "name": "repeat requires shifting the window",
        "input": "pwwkew",
        "expected": 3,
    },
    {
        "name": "empty string",
        "input": "",
        "expected": 0,
    },
    {
        "name": "single character",
        "input": "a",
        "expected": 1,
    },
    {
        "name": "all unique characters",
        "input": "abcdef",
        "expected": 6,
    },
    {
        "name": "overlapping repeat",
        "input": "dvdf",
        "expected": 3,
    },
    {
        "name": "palindromic repeat",
        "input": "abba",
        "expected": 2,
    },
    {
        "name": "longest substring at the end",
        "input": "tmmzuxt",
        "expected": 5,
    },
    {
        "name": "repeat at the start",
        "input": "aab",
        "expected": 2,
    },
    {
        "name": "single space",
        "input": " ",
        "expected": 1,
    },
    {
        "name": "repeated spaces",
        "input": "a b a",
        "expected": 3,
    },
    {
        "name": "unicode characters",
        "input": "你好世界你",
        "expected": 4,
    },
    {
        "name": "case-sensitive characters",
        "input": "aA1!a",
        "expected": 4,
    },
    {
        "name": "longest substring after an early repeat",
        "input": "anviaj",
        "expected": 5,
    },
]


def find_longest_substring(s: str) -> int:

    if len(s) == 0:
        return 0
    
    left = 0
    seen = set()

    best = 0

    for right in range(len(s)):

        cur_char = s[right]

        while cur_char in seen:
            seen.remove(s[left])
            left += 1
        
        seen.add(cur_char)

        cur_length = right - left + 1

        best = max(cur_length, best)
            
    return best


def print_test_result(index: int, name: str, passed: bool, details: dict[str, object]) -> int:
    status = "PASSED" if passed else "FAILED"
    print(f"Test {index}: {status} - {name}")

    if not passed:
        for label, value in details.items():
            print(f"  {label}: {value}")

    return int(passed)


passed_tests = 0

for index, test in enumerate(test_cases, start=1):
    result = find_longest_substring(test["input"])
    passed_tests += print_test_result(
        index,
        test["name"],
        result == test["expected"],
        {
            "input": repr(test["input"]),
            "expected": test["expected"],
            "got": result,
        },
    )

print(f"Summary: {passed_tests}/{len(test_cases)} tests passed")
