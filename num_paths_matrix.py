"""
Count all the paths from left top corner to right bot­tom corner in two dimensional array.

If the array value is 1, the path can be taken, if 0, it cannot, and all paths move down or right.
"""


def number_of_paths(n, m, in_arr):
    count = [[0 for s in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            if in_arr[i][j] == 1:
                if i == 0 and j == 0:
                    count[0][0] = 1
                elif i == 0 and j > 0:
                    count[0][j] = count[0][j-1]
                elif j == 0 and i > 0:
                    count[i][0] = count[i-1][0]
                else:
                    count[i][j] = count[i-1][j] + count[i][j-1]
    return count[n-1][m-1] % (10**9 + 7)

if __name__ == '__main__':
    print(number_of_paths(3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    print(number_of_paths(3, 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
    print(number_of_paths(3, 3, [[1, 1, 0], [1, 1, 1], [0, 0, 1]]))
    print(number_of_paths(3, 3, [[1, 1, 0], [1, 1, 0], [0, 1, 1]]))