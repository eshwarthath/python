#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s1=list(s)
    s1[0]=s[0].upper()
    for i in range (len(s)-1):
 
        if s1[i]==" ":
            s1[i+1]=s[i+1].upper()
    return ''.join(s1)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
