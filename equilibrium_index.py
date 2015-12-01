# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution1(A):
    # write your code in Python 2.7
    if len(A) > 1:
        sumA = reduce(lambda x,y : x + y, A)
    else:
        return 0
    for idx, e in enumerate(A):
        if (sum - e) % 2 != 0:
            continue
        else:
            half = float((sum - e) / 2)
            lowerSum = reduce(lambda x,y: x+y, A[:idx]) if len(A[:idx]) > 0 else 0
            if ( lowerSum - half) == 0:
                return idx
    
    return -1

def solution(A):
    if len(A) > 1:
        sumA = reduce(lambda x,y : x + y, A)
        lowerSum = 0
        for idx, e in enumerate(A):
            lowerSum += A[idx - 1] if idx > 0 else 0
            if (lowerSum - (sumA-e)/2.0) == 0:
                return idx
    elif len(A) == 1:
        return 0
    
    return -1
