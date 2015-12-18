def max_slice(A):
	n = len(A)
	#max_end: largest sum that ends at that position k
	#max_end at k + 1 = max(max_end_k + A[k+1], A[k+1] )
	max_end = max_sum = 0
	for k in xrange(n):
		max_end = max(A[k], max_end+A[k])
		max_sum = max(max_sum, max_end)
	return max_sum

print max_slice([5,-7,3,5,-2,4,-1])