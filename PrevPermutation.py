"""
Find the previous permutation for a set of numbers.
E.g. 3,4,1,2,5 -> 3,2,5,4,1
"""
numbers = [3, 4, 1, 2, 5]


def reverse(nums, i):
    j = len(nums) - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


def prev_permutation(nums):
    if len(nums) < 2:
        return nums

    i = len(nums) - 2
    while i >= 0 and nums[i] < nums[i + 1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while j > 0 and nums[j] > nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    reverse(nums, i + 1)
    return nums


def main():
    result = prev_permutation(numbers)
    print(result)


if __name__ == "__main__":
    main()
