"""
https://leetcode.com/problems/reshape-the-matrix

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Note:
    1. The height and width of the given matrix is in range [1, 100].
    2. The given r and c are all positive.
"""


def matrix_reshape(nums, r, c):
    """
    nums = m x n
    output_matrix = r x c
    
    for one dimension
    A[i] = M[i/n][i%n]
    thus for two dimensions
      r x c     m  x  n
    A[i][j] = M[(i*c + j) / n][(j+i*c) % n]
    
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    m = len(nums)
    n = len(nums[0])
    if r * c != m * n or (r == m and c == n):
        return nums

    return [[nums[int((j + i * c) / n)][(j + i * c) % n] for j in range(c)] for i in range(r)]

if __name__ == '__main__':
    print("""
    Example 1:
        Input: 
        nums = 
        [[1,2],
         [3,4]]
        r = 1, c = 4
        Output: 
        [[1,2,3,4]]
        Explanation:
        The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
    Example 2:
        Input: 
        nums = 
        [[1,2],
         [3,4]]
        r = 2, c = 4
        Output: 
        [[1,2],
         [3,4]]
        Explanation:
        There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
    """)

    print(matrix_reshape([[1,2],[3,4]], 1, 4))
    print(matrix_reshape([[1, 2], [3, 4]], 2, 4))
    print(matrix_reshape([[1, 2], [3, 4]], 4, 1))
