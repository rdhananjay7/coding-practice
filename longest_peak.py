def longest_peak(array):
    # O(n) time | O(1) space
    # where n is the number of elements in the array

    peak_len = 0

    for idx in range(1, len(array) - 1):
        previous = array[idx - 1]
        current = array[idx]
        next_item = array[idx + 1]

        if is_peak(previous, current, next_item):
            current_peak = 1
            left = idx - 1
            right = idx + 1

            while left >= 0:

                if left >= 1 and array[left] == array[left - 1]:
                    current_peak += 1
                    break

                if array[left] < array[left + 1]:
                    current_peak += 1
                    left -= 1
                else:
                    break

            while right <= len(array) - 1:

                if right <= len(array) - 2 and array[right] == array[right + 1]:
                    current_peak += 1
                    break

                if array[right] < array[right - 1]:
                    current_peak += 1
                    right += 1
                else:
                    break

            peak_len = max(peak_len, current_peak)

    return peak_len


def is_peak(previous, current, next_item):
    return current > previous and current > next_item


if __name__ == "__main__":

    print(longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
    print(longest_peak([1, 3, 2]))
