# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    n = len(A)
    size = 0
    for k in xrange(n):
        if size > 0 and A[k] != candidate:
            size -= 1
        else:
            size += 1
            candidate = A[k]
    countEquil = 0
    if size > 0:
        countTotal = 0
        for k in xrange(n):
            if A[k] == candidate:
                countTotal += 1
        if countTotal > n/2:
            leader = candidate
            n1 = 0
            numLeader1 = 0
            for k in xrange(n):
                n1 += 1
                if A[k] == leader: numLeader1 += 1
                if numLeader1 > n1/2 and (countTotal - numLeader1) > (n-n1)/2: countEquil += 1
    
    return countEquil