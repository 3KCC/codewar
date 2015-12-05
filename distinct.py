# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    n = len(A)
    A.sort()
    count = 0
    for i in xrange(0,n):
        if i == 0 or A[i] > curr:
            curr = A[i]
            count += 1
    return count