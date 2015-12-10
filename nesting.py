# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    # write your code in Python 2.7
    n = len(S)
    closes = 0
    opens = 0
    for x in S:
        if x == '(':
            opens += 1
        if x == ')':
            closes += 1
        if closes > opens:
            return 0
    return 1 if opens == closes else 0
