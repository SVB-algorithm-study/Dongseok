#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    m = 0
    M = 0
    arr.sort()
    for i in range(len(arr)-1):
        m += arr[i]
    for i in range(1,len(arr)):
        M += arr[i]
        
    print(m,M)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
