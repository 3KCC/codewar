def count_total(A,x,y):
	n = len(A)
	P = [0]*(n+1)
	for i in xrange(1,n+1):
		P[i] = P[i-1] + A[i-1]
	return P[y+1] - P[x]

def mushroomPicker(A,k,m):
	n = len(A)
	P = [0]*(n+1)
	P[k] = A[k]
	for i in xrange(k+1,n):
		P[i] = P[i-1] + A[i]
	for i in xrange(k-1,-1,-1):
		P[i] = P[i+1] + A[i]
	maximal = P[k]
	for i in xrange(min(m,n-k)):
		j = m-2*i
		if j < k:
			curr = P[k+i] + P[j] - P[k]
			if maximal < curr : maximal = curr
	return maximal

def mushroomPicker2(A,k,m):
	n = len(A)
	result = 0
	for i in xrange(min(m,k) + 1):
		left_pos = k - i
		right_pos = min(n - 1, max(k, k + m - 2*i))
		result = max(result, count_total(A, left_pos, right_pos))

	#either
	for i in xrange(min(m,n-k) + 1):
		right_pos = k + i
		left_pos = min(0, max(k, k - (m - 2*i)))
		result = max(result, count_total(A, left_pos, right_pos))

	return result

#print count_total([1,2,3],1,2)
print mushroomPicker2([2,3,7,5,1,3,9], 4, 6)