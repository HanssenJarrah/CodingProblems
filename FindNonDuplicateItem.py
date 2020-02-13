""" Given an unordered array of duplicate numbers, find the non-duplicate item. """
arr = [1, 6, 2, 3, 2, 1, 6, 0, 0]


def find_non_duplicate(array):
    non_duplicate = array[0]
    for i in range(1, len(array)):
        non_duplicate ^= array[i]

    return non_duplicate


def main():
    result = find_non_duplicate(arr)
    print(result)


if __name__ == "__main__":
    main()