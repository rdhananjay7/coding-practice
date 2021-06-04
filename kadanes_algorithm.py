def kadanes_algorithm(array):
    # O(n) time | O(1) space

    max_so_far = float("-inf")
    max_ending_here = float("-inf")

    for idx in range(len(array)):
        max_ending_here = max(max_ending_here + array[idx], array[idx])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


if __name__ == "__main__":
    # arr = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
    arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    print(kadanes_algorithm(arr))