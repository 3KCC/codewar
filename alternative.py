def solution(A):
	n = len(A)
	maximal = 0
	current = 1
	direction = 0
	for i in xrange(1,n):
		if (A[i] - A[i-1])*direction < 0 or (direction == 0 and A[i] - A[i-1] != 0):
			current += 1
		else:
			if current > maximal:
				maximal = current
			current = 1 if A[i] == A[i-1] else 2
		direction = A[i] - A[i-1]
	return max(maximal,current)

print solution([0,0,0,1,2,-1,5,5])