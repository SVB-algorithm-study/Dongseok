#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    answer = []
    scoreMin = scores[0]
    scoreMax = scores[0]
    mC = 0
    MC = 0
    for i in range(1, len(scores)):
        if scoreMax < scores[i]:
            MC += 1
            scoreMax = scores[i]
        elif scoreMin > scores[i]:
            mC += 1
            scoreMin = scores[i]
    answer.append(MC)
    answer.append(mC)
    return answer
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
