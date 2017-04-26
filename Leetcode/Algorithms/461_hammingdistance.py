"""
https://leetcode.com/problems/hamming-distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
"""


def hamming_distance_kernighan(x, y):
    """
    Using Brian Kernighan's algorithm to clear the least significant bit that is set, can count number of 1's
    :type x: int
    :type y: int
    :rtype: int
    """
    value = x ^ y  # gets where corresponding bits are different
    count = 0
    while value:
        count += 1
        value &= value - 1  # Clears least significant bit set
    return count


def hamming_distance_count(x, y):
    """
    Using Python's count method change x ^ y 0bxxxx form (string) and then count number of 1s
    :type x: int
    :type y: int
    :rtype: int
    """
    return bin(x ^ y).count('1')

if __name__ == "__main__":
    print("""
    Input: x = 1, y = 4

    Output: 2

    Explanation:
    1   (0 0 0 1)
    4   (0 1 0 0)
           ↑   ↑

    The above arrows point to positions where the corresponding bits are different.
    """)
    print(descript)

    print(hamming_distance_kernighan(1, 4))
    print(hamming_distance_count(1, 4))
