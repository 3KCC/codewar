def solution_n2(A):
	n = len(A)
	P = [0]*(n+1)
	for i in xrange(1,n+1):
		P[i] = P[i-1] + A[i-1]
	avg = [0]*(n-1)
	for i in xrange(n-1):
	    avg[i] = min([(P[i+k] - P[i])*1.0/k for k in xrange(2,n-i+1)])
	return avg.index(min(avg))

#only need to check sum of 2 or 3 of length
#assume: m > 3 => break into 2s and 3s  and all have same average
def solution(A):
	n = len(A)
	minAvg = min(sum(A[:2])/2.0,sum(A[:3])/3.0)
	idx = 0
	for i in xrange(1, n-2):
		currentAvg = min(sum(A[i:i+2])/2.0, sum(A[i:i+3])/3.0)
		if minAvg > currentAvg:
			idx = i
			minAvg = currentAvg
	return n-2 if minAvg > sum(A[-2:])/2.0 else idx

print solution([4,2,2,5,1,5,8])
