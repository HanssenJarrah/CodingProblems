"""
Find the integer that occurs most frequently in num_arr. If there are multiple numbers that occurs with the
same frequency, just return one of them.
"""
num_arr = [3, 1, 4, 57, 4]


def most_frequent_int(array):
    if len(array) == 0:
        return None

    num_freq = {}
    for item in array:
        if item in num_freq:
            num_freq[item] += 1
        else:
            num_freq[item] = 1

    most_frequent_num = array[0]
    freq = num_freq[most_frequent_num]
    for num in num_freq:
        new_freq = num_freq[num]
        if new_freq > freq:
            most_frequent_num = num
            freq = new_freq

    return most_frequent_num


def main():
    result = most_frequent_int(num_arr)
    print(result)


if __name__ == "__main__":
    main()