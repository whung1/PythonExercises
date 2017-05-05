"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""


def find_disappeared_numbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # if a number ever appears, use it as index and set nums[num] as negative. Then iterate through and whatever is
    # positive cannot be in the array
    for num in nums:
        if nums[abs(num) - 1] > 0:
            nums[abs(num) - 1] *= -1
    return [i+1 for i in range(len(nums)) if nums[i] > 0]

if __name__ == '__main__':
    print("""
    Example:

    Input:
    [4,3,2,7,8,2,3,1]
    
    Output:
    [5,6]
    """)
    print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))
