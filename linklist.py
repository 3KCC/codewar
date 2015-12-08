def solution(A):
	l = 1
	i = 0
	while A[i] != -1:
		l += 1
		i = A[i]
	return l
	print solution([1,2,5,0,9,-1,7])
