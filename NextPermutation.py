"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order.
The replacement must be in-place and use only constant extra memory.
E.g. 2,5,1 -> 5,1,2
"""
numbers = [5, 2, 1]


def reverse(nums, i):
    j = len(nums) - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


def next_permutation(nums):
    if len(nums) < 2:
        return nums

    i = len(nums) - 2
    while i >= 0 and nums[i] > nums[i + 1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while j > i and nums[j] < nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    reverse(nums, i + 1)
    return nums


def main():
    result = numbers
    for i in range(6):
        result = next_permutation(result)
        print(result)


if __name__ == "__main__":
    main()