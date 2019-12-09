#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Imraj423"

import sys


def main(args):
    left = "({["  # opening delimiters
    right = ")}]"  # respective closing delims
    S = []
    for i in args:
        if i in left:
            S.append(i)  # push left delimiter on stack
        elif i in right:
            if not S:
                return False  # nothing to match with
            if right.index(i) != left.index(S.pop()):
                return False  # mismatched
    if not S:
        return True
    else:
        return False


num_cases = int(input())
while num_cases:
    # input_text = raw_input()
    if (main(raw_input()) == True):
        print("YES")
    else:
        print("NO")
    num_cases = num_cases - 1


if __name__ == '__main__':
    main(sys.argv)
