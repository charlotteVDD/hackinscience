# -*- coding: utf-8 -*-
"""
function is_multiple(a, b) that takes 2 arguments
return True if a is a multiple of b, otherwhise False.
@author: CharlotteVDD
"""


def is_multiple(a, b):
    if a % b == 0:
        return True
    return False

print(is_multiple(6, 3))
print(is_multiple(889, 15))
print(is_multiple(15, 45))
