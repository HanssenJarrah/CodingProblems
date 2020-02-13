"""
Find all the pairs of integers in a list that sum to a given number.
Once a number from the list has been used, it cannot be used again.
"""
num_arr = [1, 2, 1, 3, 0]


def find_pairs_that_sum(array, n):
    if len(array) == 0:
        return None

    num_freq = {}
    for item in array:
        if item in num_freq:
            num_freq[item] += 1
        else:
            num_freq[item] = 1

    pairs = []
    for num in array:
        if n - num in num_freq:
            if num_freq[num] > 0 and num_freq[n - num] > 0:
                num_freq[n - num] -= 1
                num_freq[num] -= 1
                pairs.append((num, n - num))
    return pairs


def main():
    result = find_pairs_that_sum(num_arr, 3)
    for item1, item2 in result:
        print(item1, item2)


if __name__ == "__main__":
    main()