# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution_40(N, A):
    # write your code in Python 2.7
    counter = [0]*N
    for i in range(len(A)):
        if A[i] <= N and A[i] >= 1:
            counter[A[i]-1] += 1
        elif A[i] == N + 1:
            counter = [max(counter)]*N
    return counter

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution_60(N, A):
    # write your code in Python 2.7
    counter = [0]*N
    maxC = 0
    for i in range(len(A)):
        if A[i] <= N and A[i] >= 1:
            counter[A[i]-1] += 1
            if counter[A[i]-1] > maxC:
                maxC = counter[A[i]-1]
        elif A[i] == N + 1:
            counter = [maxC]*N
    return counter

def solution(N, A):
    # write your code in Python 2.7
    counter = [0]*N
    maxC = 0
    minC = 0
    for i in range(len(A)):
        if A[i] <= N and A[i] >= 1:
            counter[A[i]-1] = minC + 1 if minC > counter[A[i]-1] else counter[A[i]-1] + 1
            if counter[A[i]-1] > maxC:
                maxC = counter[A[i]-1]
        elif A[i] == N + 1:
            minC = maxC
    return [max(e,minC) for e in counter]