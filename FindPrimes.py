""" Create a function that takes a list of numbers and returns a new list containing only prime numbers."""
"""
# Determines if any elements of any array are duplicates:
def duplicates(array):
    item_set = set()
    for item in array:
        if item in item_set:
            return True
        item_set.add(item)
    return False
"""


lst = [1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]


# Checks if a given number is a prime number
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    # This is checked so that we can skip
    # middle five numbers in below loop
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i = i + 6
    return True


def filter_primes(num_list):
    # num_set = set(num_list)
    items = []
    for item in num_list:
        if is_prime(item):
            items.append(item)
    return items


def main():
    primes = filter_primes(lst)
    print(primes)
    print("[1009, 3, 61, 1087, 1091, 1093, 1097] is the correct answer")


if __name__ == "__main__":
    main()
