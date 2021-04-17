def is_monotonic(array):
    # O(n) time | O(1) space
    # A little complex Brute force can be found commented below

    is_non_decreasing = True
    is_non_increasing = True

    for idx in range(1, len(array)):

        if array[idx] > array[idx - 1]:
            is_non_decreasing = False
        elif array[idx] < array[idx - 1]:
            is_non_increasing = False

    return is_non_increasing or is_non_decreasing


if __name__ == "__main__":
    print(is_monotonic([-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -8, -9, -10, -11]))
    print(is_monotonic([1, 1, 2, 2, 3, 4, 5, 6, 12, 7]))

"""
    direction = ""

    for idx in range(len(array)):
        current_direction = ""
        if array[idx] == array[idx - 1]:
            continue
        elif array[idx] > array[idx - 1]:
            current_direction = "INCREASING"
        else:
            current_direction = "DECREASING"

        if direction != "" and direction != current_direction:
            return False
        else:
            direction = current_direction

    return True
"""
