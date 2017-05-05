"""
https://leetcode.com/problems/find-all-duplicates-in-an-array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
"""


def find_duplicates(nums):
    """
    XOR is unhelpful here due to the fact that just because we cant track what numbers "disappear" due to it, we can
    only keep track of leftover bits that are the amalgamation of all the numbers
     
    Thus, we can use the problem constraints "1 ≤ a[i] ≤ n (n = size of array)" to reuse the array to save space, while
    keeping track of times of appearance
    
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = []
    for num in nums:
        if nums[abs(num) - 1] < 0:
            ans.append(abs(num))
        else:
            nums[abs(num) - 1] *= -1
    return ans

if __name__ == '__main__':
    print("""
    Example:

    Input:
    [4,3,2,7,8,2,3,1]
    
    Output:
    [2,3]
    """)

    print(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))