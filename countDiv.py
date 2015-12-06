# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, B, K):
    # write your code in Python 2.7
    if A%K == 0:
        result = (B-A)/K + 1
    else:
        result = (B - (A + K - A%K))/K + 1
    return  result