def largest_range(array):
    # O(n) time | O(n) space
    hashmap = {}
    for number in array:
        if number not in hashmap:
            hashmap[number] = False

    min_range, max_range = None, None
    for idx, number in enumerate(array):
        if hashmap[number]:
            continue
        else:

            hashmap[number] = True

            left, right = number, number
            if left - 1 in hashmap or right + 1 in hashmap:
                while True:
                    if left - 1 in hashmap:
                        left -= 1
                        hashmap[left] = True
                    else:
                        break

                while True:
                    if right + 1 in hashmap:
                        right += 1
                        hashmap[right] = True
                    else:
                        break

            if min_range is None:
                min_range = left
                max_range = right
            else:
                if max_range - min_range < right - left:
                    min_range = left
                    max_range = right

    print(hashmap)
    print([min_range, max_range])
    return [min_range, max_range]


if __name__ == "__main__":
    print(largest_range([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
    print(largest_range([10, 0, 1]))
