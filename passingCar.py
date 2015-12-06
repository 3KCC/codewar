# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    n = len(A)
    count = 0
    increment = 0
    for i in xrange(n):
        if count > 1000000000:
            return -1
        if A[i] == 0:
            increment += 1
        if A[i] == 1:
            count += increment
    return count