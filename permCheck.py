# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    n = check = len(A)
    perm = [0]*n
    for e in A:
        if e > n or perm[e-1] == 1:
            return 0
        else:
            perm[e-1] += 1
            check -= 1
    if check == 0:
        return 1
    return 0
