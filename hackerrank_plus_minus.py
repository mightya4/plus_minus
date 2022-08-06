#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    len_of_array = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    pos = pos / len_of_array
    neg = neg / len_of_array
    zero = zero / len_of_array
    
    #Format output of each fraction with 6 decmal places after decimal
    print("{:.6f}".format(pos))
    print("{:.6f}".format(neg))
    print("{:.6f}".format(zero))
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
