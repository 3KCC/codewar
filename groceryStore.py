def groceryStore(A):
	n = len(A)
	numPp = 0
	minPp = 0
	for i in xrange(n):
		if A[i] == 1:
			numPp -= 1
			if numPp < 0:
				minPp += 1
				numPp = 0
		else:
			numPp += 1
	return minPp
print groceryStore([1,1,1,1])
