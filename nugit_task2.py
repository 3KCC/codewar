def solution(A,x):
	#n2 - k2 = k1 => n2 = k1 + k2 = k
	n = len(A)
	numOfx = 0
	for i in xrange(n):
		if A[i] == x:
			numOfx += 1
	return n - numOfx

print solution([5,5,0], 5)
