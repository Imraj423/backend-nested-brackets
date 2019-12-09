#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Imraj423"


import sys

openers = ['(', '<', '{', '[', '(*']
closers = [')', '>', '}', ']', '*)']


def is_nested(line):
    stack = []
    count = 0
    matching_opener = ''
    while line:
        token = line[0]
        if line[:2] == '(*':
            token = '(*'
        if line[:2] == '*)':
            token = '*)'
        count += 1

        if token in openers:
            stack.append(token)
        if token in closers:
            i = closers.index(token)
            matching_opener = openers[i]
            if stack and stack.pop() != matching_opener:
                return count

        line = line[len(token):]

    if stack:
        return count
    return 0


def main(args):
    # print(args)
    with open(args[1]) as f:
        text_list = f.read().split('\n')
    print(text_list)
    # text_list = open(args[1]).read().split('\n')

    with open('output.txt', 'w') as f:

        for i in text_list:
            result = is_nested(i)
            if result > 0:
                f.write("NO {} \n".format(result))
                print("NO {}".format(result))

            else:
                print("YES")
                f.write("YES \n")


if __name__ == '__main__':

main(sys.argv)
# import sys


# def main(args):
#     left = "({["  # opening delimiters
#     right = ")}]"  # respective closing delims
#     S = []
#     for i in args:
#         if i in left:
#             S.append(i)  # push left delimiter on stack
#         elif i in right:
#             if not S:
#                 return False  # nothing to match with
#             if right.index(i) != left.index(S.pop()):
#                 return False  # mismatched
#     if not S:
#         return True
#     else:
#         return False


# num_cases = int(input())
# while num_cases:
#     # input_text = raw_input()
#     if (main(raw_input()) == True):
#         print("YES")
#     else:
#         print("NO")
#     num_cases = num_cases - 1


# if __name__ == '__main__':
#     main(sys.argv)
