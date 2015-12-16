def n2_solution(A):
	n = len(A)
	for i in xrange(n):
		count = 0
		for j in xrange(n):
			if A[j] == A[i]: count += 1
		if count > n/2: return A[i]
	return -1

def nlogn_solution(A):
	n = len(A)
	A.sort()
	candidate = A[n/2]
	count = 0
	for i in xrange(n):
		if A[i] == candidate:
			count += 1
	return -1 if count <= n/2 else candidate

def n_solution(A):
	n = len(A)
	candidate = None
	for i in xrange(n):
		if candidate and A[i] != candidate:
			candidate = None
		else:
			candidate = A[i]
	if candidate:
		count = 0
		for i in xrange(n):
			if A[i] == candidate:
				count += 1
	return candidate if count > n/2 else -1


print n_solution([6,8,4,6,8,6,6])