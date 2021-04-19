"""
Given an array of integers arr, write a function that returns true if and only if
the number of occurrences of each value in the array is unique.

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

"""

from collections import Counter


def unique_number_of_occurrences(array):
    # O(n) where n is the number of elements in the array

    hashmap = Counter(array)
    counts = hashmap.values()
    unique_counts = set(counts)

    return len(counts) == len(unique_counts)


if __name__ == "__main__":
    input_array = [1, 2, 2, 1, 1, 3]
    print(unique_number_of_occurrences(input_array))
