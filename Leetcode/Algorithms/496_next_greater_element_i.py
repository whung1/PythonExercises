"""
https://leetcode.com/problems/next-greater-element-i

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. 
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. 
If it does not exist, output -1 for this number.
"""
from collections import deque


def next_greater_element_brute(findNums, nums):
    """
    Brute force method to find next greater element by linear searching every time for next greater element
    runtime: O(n^2)
    
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    out_list = [-1]*len(findNums)
    for i in range(len(findNums)):
        match_index = -1  # index of findNums[i] in nums
        for j in range(len(nums)):
            if match_index != -1 and nums[match_index] < nums[j]:
                out_list[i] = nums[j]
                break
            elif findNums[i] == nums[j]:  # match_index has not been found
                match_index = j
    return out_list


def next_greater_element_stack(findNums, nums):
    """
    Using a stack to populate a dictionary with each element of nums' greater element
    runtime: O(n)

    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    # Setup dictionary
    stack = deque()
    dict = {}  # Since we know values are distinct, one value will have one greater element
    for value in nums:
        while len(stack) and stack[-1] < value:
            dict[stack.pop()] = value
        stack.append(value)

    # Iterate through findNums and using dictionary to search, create output list
    out_list = [-1] * len(findNums)
    for i in range(len(findNums)):
        if findNums[i] in dict:
            out_list[i] = dict[findNums[i]]
    return out_list


if __name__ == "__main__":
    descript = """
    You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

    The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
    
    Example 1:
        Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
        Output: [-1,3,-1]
        Explanation:
            For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
            For number 1 in the first array, the next greater number for it in the second array is 3.
            For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
    Example 2:
        Input: nums1 = [2,4], nums2 = [1,2,3,4].
        Output: [3,-1]
        Explanation:
            For number 2 in the first array, the next greater number for it in the second array is 3.
            For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
    Note:
        1. All elements in nums1 and nums2 are unique.
        2. The length of both nums1 and nums2 would not exceed 1000.
    """
    print(descript)

    print(next_greater_element_brute([4, 1, 2], [1, 3, 4, 2]))
    print(next_greater_element_brute([2, 4], [1, 2, 3, 4]))
    print(next_greater_element_stack([4, 1, 2], [1, 3, 4, 2]))
    print(next_greater_element_stack([2, 4], [1, 2, 3, 4]))
