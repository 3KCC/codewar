# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    if len(A) > 1:
        totalSum = reduce(lambda x,y: x+y, A)
        leftSum = 0
        for idx, e in enumerate(A):
            if idx > 0:
                leftSum += A[idx-1]
                newDif = abs(totalSum-2*leftSum)
                if idx == 1 or newDif < minDif:
                    minDif = newDif
        return minDif
    elif len(A) == 1:
        return A[0]
    else:
        return 0
