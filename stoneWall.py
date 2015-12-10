# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(H):
    # write your code in Python 2.7
    n = len(H)
    stack = []
    numOfBricks = 0
    for i in xrange(n):
        if len(stack) != 0:
            if H[i] > stack[-1]:
                stack.append(H[i])
                numOfBricks +=1
            elif H[i] < stack[-1]:
                while len(stack) > 0 and H[i] < stack[-1]:
                    stack.pop()
                if len(stack) == 0 or H[i] > stack[-1]:
                    stack.append(H[i])
                    numOfBricks += 1
        else:
            numOfBricks += 1
            stack.append(H[i])
    return numOfBricks

#same idea but work with stack initiated with n 0s
def solution2(H):
    n = len(H)
    stack = [0]*n
    stones = 0
    stackNum = 0

    for i in xrange(n):
        #if stackNum = 0, simply skip while loop
        #if H[i] >= stack[stackNum-1], skip while loop too
        while stackNum > 0 and H[i] < stack[stackNum-1]:
            #pop
            stackNum -= 1
            #stack[stackNum-1] = 0, optional
        if stackNum > 0 and H[i] == stack[stackNum-1]:
            pass
        else:
            #push
            stack[stackNum] = H[i]
            stackNum += 1
            stones += 1
    return stones
