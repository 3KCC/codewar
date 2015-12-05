# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    n = len(A)
    A.sort()
    for i in xrange(n-1):
        for j in xrange(i+1, n-1):
            if A[i]+A[j] > A[j+1]:
                return 1 
    return 0

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    n = len(A)
    A.sort()
    for i in xrange(n-2):
        if A[i]+A[i+1] > A[i+2]:
            return 1 
    return 0