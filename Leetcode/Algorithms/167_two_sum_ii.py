"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.
"""


def two_sum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    # since we know solution exists, move index appropriately since we know list order
    low = 0
    high = len(numbers) - 1
    t_sum = numbers[low] + numbers[high]
    while t_sum != target:
        if t_sum < target:
            low += 1
        elif t_sum > target:
            high -= 1
        t_sum = numbers[low] + numbers[high]
    return [low+1, high+1]  # offset by one for the index to return

if __name__ == '__main__':
    print("""
    Input: numbers={2, 7, 11, 15}, target=9
    Output: index1=1, index2=2
    """)

    print(two_sum([2, 7, 11, 15], 9))
