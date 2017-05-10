"""
https://leetcode.com/problems/move-zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


def move_zeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = 0
    while i < len(nums) and j < len(nums):
        # if the current value is on a zero, we know there's no point of swapping behind us
        # if the current value is on a number, we know that we can swap behind us since it will either only swap with
        # itself or a zero
        if nums[i] != 0:
            # swap
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            j += 1
        i += 1
    return nums

if __name__ == '__main__':
    print("""
    nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
    """)

    print(move_zeroes([0, 1, 0, 3, 12]))
