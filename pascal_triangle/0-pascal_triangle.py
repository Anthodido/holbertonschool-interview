#!/usr/bin/python3

"""Pascal's Triangle module."""

def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = []
    for j in range (1, n +1):
        row = [1] * j
        for i in range(1, j - 1):
            row[i] = triangle[j - 2][i - 1] + triangle[j - 2][i]
        triangle.append(row)
    return triangle
