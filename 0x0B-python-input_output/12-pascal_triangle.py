#!/usr/bin/python3
"""creation of Pascal triangle"""


def pascal_triangle(n):
    """
    defines pascals triangle and returns a list of
    lists of integers representing the Pascal’s triangle of n:
    """

    if n <= 0:
        return []
    triangle = [[1]]
    for j in range(1, n):
        row = [1]
        prev_row = triangle[j - 1]

        for i in range(1, j):
            row.append(prev_row[i - 1] + prev_row[i])

        row.append(1)
        tringle.append(row)
    return triangle
