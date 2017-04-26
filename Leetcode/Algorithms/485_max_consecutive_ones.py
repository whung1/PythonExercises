"""
https://leetcode.com/problems/max-consecutive-ones

Given a binary array, find the maximum number of consecutive 1s in this array.

Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""


def find_max_consecutive_ones_brute(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    final = 0
    for i in range(len(nums)):
        if nums[i]:
            count += 1
            final = max(count, final)
        else:
            count = 0
    return final


def find_max_consecutive_ones_to_str(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    num_str = ''.join(map(str, nums))
    seperated = num_str.split('0')
    return len(max(seperated))


if __name__ == '__main__':
    """
    Input: [1,4,3,2]

    Output: 4
    Explanation: n is 2, and the maximum sum of pairs is 4.
    """
    print(find_max_consecutive_ones_brute([1,4,3,2]))
    print(find_max_consecutive_ones_to_str([1,4,3,2]))
