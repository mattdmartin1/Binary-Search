# New File

# Binary search vs regular search
# list and target
# dividing number in half and ><=

import random
import time

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
        else:
            return -1

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    elif high is None:
        high = len(l) - 1
    if high < low:
        return -1
    
    midpoint = (low + high) // 2
    
    if len[l] == midpoint:
        return midpoint 
    elif target < l[midpoint]:
        return binary_search(l ,target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)
    
    # testing