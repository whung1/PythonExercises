"""
https://leetcode.com/problems/minimum-moves-to-equal-array-elements

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

    Input:
    [1,2,3]
    
    Output:
    3
    
    Explanation:
    Only three moves are needed (remember each move increments two elements):
    
    [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""


def min_moves(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Adding 1 to all the bars in the initial state does not change the initial state - it simply shifts the initial state uniformly by 1.
    # This gives us the insight that a single move is equivalent to subtracting 1 from any one element with respect to the goal of reaching a final state with equal heights.
    # Since min(nums) * n = sum(nums), if we add +1 to num k times, min(nums) * n = sum(nums) - k
    # k = sum(nums) - min(nums) * n
    return sum(nums) - min(nums)*len(nums)

if __name__ == '__main__':
    print("""
    Example:

    Input:
    [1,2,3]
    
    Output:
    3
    
    Explanation:
    Only three moves are needed (remember each move increments two elements):
    
    [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
    
    Example:

    Input:
    [0,2,3]
    
    Output:
    5
    """)

    print(min_moves([1,2,3]))
    print(min_moves([0,2,3]))

