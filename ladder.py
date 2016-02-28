# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, B):
    # write your code in Python 2.7
    n = len(A)
    result = []
    for k in xrange(n):
        result.append(fib(A[k]) % 2**(B[k]))
    return result
            
def fib(n):
    fib = [0]*(n+2)
    fib[0] = fib[1] = 1
    for k in xrange(2,n+2):
        fib[k] = fib[k-1] + fib[k-2]
    return fib[n]

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, B):
    # write your code in Python 2.7
    n = len(A)
    result = []
    fib = [1,1]
    m = 1

    for k in xrange(n):
        while A[k] > m:
            m += 1
            fib.append(fib[m-1] + fib[m-2])
        result.append(fib[A[k]] % 2**(B[k]))
    return result

def solution(A, B):
    # write your code in Python 2.7
    n = len(A)
    result = []
    fib = [0]*(n+2)
    fib[0] = fib[1] = 1
    for k in xrange(2,n+2):
        fib[k] = fib[k-1] + fib[k-2]

    for k in xrange(n):
        result.append(fib[A[k]] % 2**(B[k]))
    return result

def solution(A, B):
    # write your code in Python 2.7
    n = len(A)
    L = max(A)
    result = []
    fib = [0]*(n+2)
    fib[0] = fib[1] = 1
    for k in xrange(2,L+2):
        fib[k] = fib[k-1] + fib[k-2]

    for k in xrange(n):
        result.append(fib[A[k]] % (1<<B[k]))
    return result

def solution(A, B):
    # write your code in Python 2.7
    n = len(A)
    L = max(A)
    maxB = max(B)
    result = []
    fib = [0]*(n+2)
    fib[0] = fib[1] = 1
    for k in xrange(2,L+2):
        fib[k] = ( fib[k-1] + fib[k-2] ) & ((1<<maxB) - 1)

    for k in xrange(n):
        result.append(fib[A[k]] & ((1<<B[k]) - 1))
    return result