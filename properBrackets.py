def properBrackets(n, m):
	count = 0
	if m < 0 or n <= 0:
		return 0
	if m == n:
		return 1
	count += properBrackets(n-1, m+1) + properBrackets(n-1, m-1)
	return count

def properBracketsWithFixed(n, m, A, i, k):
	count = 0
	if m < 0 or n <= 0 or m > n:
		return 0
	if m == n and k >= len(A):
		return 1
	if k >= len(A) or i != A[k]:
		count += properBracketsWithFixed(n-1, m+1, A, i+1, k) + properBracketsWithFixed(n-1, m-1, A, i+1, k)
	else:
		count += properBracketsWithFixed(n-1, m+1, A, i+1, k+1)

	return count

print properBracketsWithFixed(8,0,[1,4,6],0,0)