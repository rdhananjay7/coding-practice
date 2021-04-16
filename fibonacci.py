"""
O(n) time | O(n) space where n is the number for which
fibonacci is to be calculated.
This is the top down approach to build the fibonacci.
For bottom up approach, we can bring down the space
complexity to O(1) keeping the time complexity O(n)
"""


def fib(num, memo={}):

    if num in memo:
        return memo[num]

    if num <= 2:
        return 1

    memo[num] = fib(num - 1, memo) + fib(num - 2, memo)
    return memo[num]


if __name__ == '__main__':

    print(fib(9))
