test_cases = [
    {
        "name": "Normal case",
        "prices": [7, 1, 5, 3, 6, 4],
        "expected": 5,
    },
    {
        "name": "Always decreasing",
        "prices": [7, 6, 4, 3, 1],
        "expected": 0,
    },
    {
        "name": "Always increasing",
        "prices": [1, 2, 3, 4, 5],
        "expected": 4,
    },
    {
        "name": "Single price",
        "prices": [5],
        "expected": 0,
    },
    {
        "name": "Empty list",
        "prices": [],
        "expected": 0,
    },
    {
        "name": "Best trade before global minimum",
        "prices": [2, 4, 1],
        "expected": 2,
    },
    {
        "name": "Best trade before later minimum",
        "prices": [3, 8, 1, 2],
        "expected": 5,
    },
    {
        "name": "Same prices",
        "prices": [5, 5, 5, 5],
        "expected": 0,
    },
    {
        "name": "Profit after multiple dips",
        "prices": [5, 2, 6, 1, 4],
        "expected": 4,
    },
    {
        "name": "Large profit near end",
        "prices": [9, 8, 7, 1, 10],
        "expected": 9,
    },
]

# def maximum_profit(prices: list[int]) -> int:

#     profit = 0

#     for i in range(len(prices)):

#         for j in range(i + 1, len(prices)):

#             if prices[i] < prices[j]:

#                 cur_profit = prices[j] - prices[i]

#                 if cur_profit > profit:
#                     profit = cur_profit

#     return profit


def maximum_profit(prices: list[int]) -> int:

    if len(prices) == 0:
        return 0

    best_profit = 0
    min_price = prices[0]

    for i in range(1, len(prices)):

        cur_price = prices[i]

        cur_profit = cur_price - min_price

        if cur_profit > best_profit:
            best_profit = cur_profit

        if cur_price < min_price:

            min_price = cur_price

    return best_profit


# prices = [7, 1, 5, 3, 6, 4]
# print(maximum_profit(prices=prices))

def print_test_result(index: int, name: str, passed: bool, details: dict[str, object]) -> int:
    status = "PASSED" if passed else "FAILED"
    print(f"Test {index}: {status} - {name}")

    if not passed:
        for label, value in details.items():
            print(f"  {label}: {value}")

    return int(passed)


passed_tests = 0

for index, test in enumerate(test_cases, start=1):
    result = maximum_profit(test["prices"])
    passed_tests += print_test_result(
        index,
        test["name"],
        result == test["expected"],
        {
            "prices": test["prices"],
            "expected": test["expected"],
            "got": result,
        },
    )

print(f"Summary: {passed_tests}/{len(test_cases)} tests passed")
