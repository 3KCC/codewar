# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N):
    # write your code in Python 2.7
    bN = "{0:b}".format(N)
    n = len(bN)
    max_gap = 0
    current_gap = -1
    for k in xrange(n):
        if current_gap != -1:
            if bN[k] == '0':
                current_gap += 1
            else:
                if current_gap > max_gap:
                    max_gap = current_gap
                current_gap = 0
        else:
            if bN[k] == '1':
                current_gap += 1
    return max_gap