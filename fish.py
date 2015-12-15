# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, B):
    # write your code in Python 2.7
    n = len(A)
    fishAlive = n
    upstreams = []

    for i in xrange(n):
        if B[i] == 1:
            upstreams.append(i)
        else:
            while upstreams and A[i] > A[upstreams[-1]]:
                upstreams.pop()
                fishAlive -= 1
            if upstreams:
                fishAlive -= 1
    return fishAlive