"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
"""


def array_pair_sum(nums):
    """
    Notice that if we sort the array, the max sum will always be pairing off the two lowest until the very end.
    Thus we just get the min(two lowest) each time after sorting for O(nlogn)
    :type nums: List[int]
    :rtype: int
    """
    return sum(nums.sorted()[::2])

if __name__ == '__main__':
    print("""
    Example 1:
    Input: [1,4,3,2]
    
    Output: 4
    Explanation: n is 2, and the maximum sum of pairs is 4.
    """)

    print(array_pair_sum([1,4,3,2]))