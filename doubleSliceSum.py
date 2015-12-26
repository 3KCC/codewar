# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    n = len(A)
    max_end = [0]*n
    for k in xrange(1,n-2):
        max_end[k] = max(0, max_end[k-1] + A[k])
    
    max_start = [0]*n
    for k in xrange(n-2,0,-1):
        max_start[k] = max(0, max_start[k+1] + A[k])

    max_double = 0
    for i in xrange(n-2):
        max_double = max(max_double,max_end[i] + max_start[i+2])
    
    return max_double