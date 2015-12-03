# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

#performane: 80%
def solution1(X, A):
    path = [0]*X
    for i in xrange(len(A)):
        path[A[i]-1] = 1
        if i >= X - 1 and 0 not in path:
            return i
    return -1

def solution(X, A):
    path = [0]*X
    sumPath = 0
    for i in xrange(len(A)):
        if path[A[i]-1] == 0:
	        path[A[i]-1] = 1
	        sumPath += 1
        if i >= X - 1 and sumPath == X:
            return i
    return -1
