"""
https://leetcode.com/problems/single-number

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    for num in nums:
        ans ^= num
    return ans


if __name__ == "__main__":
    print("""
    Example:
    Input: [1, 1, 2, 2, 3, 4, 4]
    Output: 3 
    """)

    print(single_number([1, 1, 2, 2, 3, 4, 4]))
