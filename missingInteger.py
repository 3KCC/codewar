# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
	n = len(A)
	check = [0]*n
	for e in A:
	    if e > 0 and e <= n:
	        if check[e-1] == 0:
	            check[e-1] = 1
	try:
	    return check.index(0) + 1
	except:
	    return n + 1
