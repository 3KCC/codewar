# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution_1(A):
    # write your code in Python 2.7
    n = len(A)
    A.append(0)
    A.sort()
    zeroIndex = A.index(0)
    A.pop(zeroIndex)
    maximal = A[-1]*A[-2]*A[-3]
    if n > 3:
        if zeroIndex > 1:
            if A[-1] > 0 and A[-2] > 0 and A[-3] > 0:
                if A[-2]*A[-3] < A[0]*A[1]: maximal = A[0]*A[1]*A[-1]
            if A[-1] > 0 and A[-2] < 0 and A[-3] < 0:
                if A[-2]*A[-3] < A[0]*A[1]: maximal = A[-1]*A[0]*A[1]
            if A[-1] > 0 and A[-2] > 0 and A[-3] < 0:
                maximal = A[-1]*A[0]*A[1]
    return maximal

def solution_1(A):
    # write your code in Python 2.7
    n = len(A)
    A.sort()
    return max(A[-1])*A[-2]*A[-3],A[-1]*A[0]*A[1]) 