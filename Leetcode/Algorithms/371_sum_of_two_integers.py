"""
https://leetcode.com/problems/sum-of-two-integers

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
"""


def get_sum(a, b):
    """
    Using xor ^ and and &, we can use xor to get the sum of any mismatched 1 and 0s, and & << 1 to carry any multiple 1s
    until there are no more carries needed.
    
    Note that negative numbers are handled due to the fact of two's complement.
    
    :type a: int
    :type b: int
    :rtype: int
    """
    mask = 0xFFFFFFFF  # masks are needed since output expects 32-bit integers and python uses 64-bit, thus mask can correct negatives etc
    MAX = 0x7FFFFFFF
    while b != 0:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    return a if a <= MAX else ~(
    a ^ mask)  # via two's complement, a^mask when > max means it converts it to its positive complement, then gets reconverted to its negative 64 bit complement

if __name__ == '__main__':
    print("""
    Example:
        Given a = 1 and b = 2, return 3.
    """)

    print(get_sum(1, 2))
    print(get_sum(-1, 1))  # for example, the positive one + negative one will make it 0 due to 0xFFFFFFFF + 0x00000001 = 0x00000000 overflow
