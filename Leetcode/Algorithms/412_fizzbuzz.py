"""https://leetcode.com/problems/fizz-buzz/#/description

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.
"""

def fizzbuzz_ifs(n):
    """
    Simple solution of if statements to create output list
    :type n: int
    :rtype: List[str]
    """
    out = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            out.append('FizzBuzz')
        elif i % 3 == 0:
            out.append('Fizz')
        elif i % 5 == 0:
            out.append('Buzz')
        else:
            out.append(str(i))
    return out

def fizzbuzz_inline_for(n):
    """
    Pythonic solution using inline for to create list
    Note that "None or value" means if None/False, then y thus it works
    :type n: int
    :rtype: List[str]
    """
    return ['Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or str(i) for i in range(1, n+1)]

if __name__ == '__main__':
    print("""
    Example:

    n = 15,

    Return:
    [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]
    """)

    print(fizzbuzz_ifs(15))
    print(fizzbuzz_inline_for(15))