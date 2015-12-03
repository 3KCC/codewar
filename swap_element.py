#A is an array containing of n integers ranged from 0..m
def counting(A,m):
	count = [0] * (m+1)
	for i in xrange(len(A)):
		count[A[i]] += 1
	return count

#|A| = |B|
#want: sum(A') = sum(B') = 1/2(sum(A)+sum(B))
#note: sum(A) - sum(B) = d => sum(A) - d/2 = sum(B) + d/2
#sum(A) - A[j] + B[i] = sum(B) + A[j] - B[i]
def swap_element(A,B,m):
	sumA = sum(A)
	sumB = sum(B)
	d = sum(A) - sum(B)
	if d%2 != 0:
		return False
	d /= 2
	count = counting(A,m)
	for i in xrange(len(B)):
		#A[j] = B[i] - d
		if 0 <= B[i] - d and B[i] - d <= m and count[B[i]-d] > 0:
			return True
	return False
