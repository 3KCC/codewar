# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

import bisect

def solution_n2(A):
    # write your code in Python 2.7
    n = len(A)
    count = 0
    for i in xrange(n):
        for j in xrange(i+1,n):
            if j-i <= A[i] + A[j]:
                count += 1
    return count

def solution_nlogn(A):
	n = len(A)
	left = [i - A[i] for i in xrange(n)]
	disc = sorted([i for i in xrange(n)], key = lambda x: left[x])
	left.sort()
	right = [2*disc[i] - left[i] for i in xrange(n)]
	count = 0
	for i in xrange(n-1):
		if count > 10000000:
			return -1
		count += bisect.bisect_right(left, right[i]) - i - 1
	return count

print solution_nlogn( [1, 5, 2, 1, 4, 0] )