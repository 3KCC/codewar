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
	size = 0
	for i in xrange(n):
		if size and A[i] != candidate:
			size -= 1
		else:
			candidate = A[i]
			size += 1
	count = 0
	if size:
		for i in xrange(n):
			if A[i] == candidate:
				count += 1
	return candidate if count > n/2 else -1

#return index
def solution(A):
    n = len(A)
    idx = -1
    size = 0
    for i in xrange(n):
    	if size != 0 and A[i] != A[idx]:
    		size -= 1
    	else:
    		idx = i
    		size += 1
    count = 0
    if size != 0:
    	for i in xrange(n):
    		if A[i] == A[idx]:
    			count += 1
    return idx if count > n/2 else -1


print n_solution([6,8,4,6,8,6,6])