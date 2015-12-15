# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    # write your code in Python 2.7
    n = len(S)
    stack = [0]*n
    opens = ['{','[','(']
    closes = ['}',']',')']
    j = -1
    for i in xrange(n):
        if S[i] in opens:
            j += 1
            stack[j] = S[i]
        if S[i] in closes:
            if stack[j] != 0 and closes.index(S[i]) == opens.index(stack[j]):
                j -= 1
            else:
                return 0
    return 1 if j == -1 else 0