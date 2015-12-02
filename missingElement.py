# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution_1(A):
    stacks = [e for e in range(1,len(A)+2)]
    for e in A:
        stacks.remove(e)
    return stacks[0]

def solution_2(A):
    for i in range(1,len(A)+2):
        if i not in A:
            return i

def solution_3(A):
    if len(A) > 0:
        fac = reduce(lambda x,y: x*y, range(1, len(A) + 2))
        product = reduce(lambda x,y: x*y, A)
        return fac/product
    else:
        return 1

def solution_4(A):
    stack = [None]*(len(A)+1)
    for e in A:
        stack[e-1] = 0
    return stack.index(None) + 1

def solution(A):
    real_sum = 1
    list_sum = 0
    for i in range(len(A)):
        real_sum += (i+2)
        list_sum += A[i]
    return real_sum - list_sum
