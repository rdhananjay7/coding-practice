def kadanes_algorithm(array):
    # O(n) time | O(1) space

    max_so_far = 0
    max_ending_here = 0

    for idx in range(len(array)):

        max_ending_here = max(max_ending_here + array[idx], array[idx])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


if __name__ == "__main__":
    arr = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
    print(kadanes_algorithm(arr))