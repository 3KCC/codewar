def solution(A,P,Q):
	n = len(A)
	nu = ['A','C','G','T']
	preSum = [[0,0,0,0]]
	current = [0]*4
	for i in xrange(n):
		k = nu.index(A[i])
		current[k] += 1
		preSum.append([]+current)
	m = len(P)
	result = []
	for j in xrange(m):
		numOfNu = map(lambda x,y: x - y, preSum[Q[j]+1], preSum[P[j]])
		result.append(numOfNu.index(not 0)+1)
	return result

print solution('ACGC',[0,1],[3,2])