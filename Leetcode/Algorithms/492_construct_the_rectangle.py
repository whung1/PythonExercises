"""
https://leetcode.com/problems/construct-the-rectangle

For a web developer, it is very important to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

1. The area of the rectangular web page you designed must equal to the given target area.

2. The width W should not be larger than the length L, which means L >= W.

3. The difference between length L and width W should be as small as possible.
You need to output the length L and the width W of the web page you designed in sequence.

Note:
    1. The given area won't exceed 10,000,000 and is a positive integer
    2. The web page's width and length you designed must be positive integers.
"""
import math


def construct_rectangle_L(area):
    """
    Increment L to find, times out since in x % n, n increases and complicates calculation time and thus runtime
    
    :type area: int
    :rtype: List[int]
    """
    L = int(math.ceil(math.sqrt(area)))
    while L < area:
        if area % L == 0:
            return [L, int(area / L)]
        L += 1
    return [None, None]

def construct_rectangle_W(area):
    """
    Similar to incrementing length, we instead decrement width to simplify modulus calculation
    
    :type area: int
    :rtype: List[int]
    """
    W = int(math.sqrt(area))
    while W > 0:
        if area % W == 0:
            return [int(area / W), W]
        W -= 1
    return [None, None]




if __name__ == '__main__':
    print("""
    Example:
    Input: 4
    Output: [2, 2]
    Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1]. 
    But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.
    """)

    print(construct_rectangle_L(4))
    print(construct_rectangle_W(4))
