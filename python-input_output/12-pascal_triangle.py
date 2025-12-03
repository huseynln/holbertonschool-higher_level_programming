#!/usr/bin/python3
"""234234"""


def fl(a):
    st = 1
    for i in range(1, a+1):
        st *= i
    return st


def pascal_triangle(n):
    """543"""

    if n <= 0:
        return []
    az = []
    it = 0
    while it < n:
        a = []
        for i in range(0, it+1):
            a.append(fl(it)//(fl(i)*fl(it-i)))
        az.append(a)
        it += 1
    return az
