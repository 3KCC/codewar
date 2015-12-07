def fib(n):
	last0 = 1
	last1 = 0
	for i in xrange(2,n):
		current = last0 + last1
		last0, last1 = current, last0
		
	return last0+last1

def binomial_recursion(n,k):
	if k > n :
		return 0
	else:
		if n == 0 or k == 0:
			return 1
	return binomial(n-1,k-1) + binomial(n-1, k)

def binomial_dynamic(n,k):
	pascal = [ [0]*(i+1) for i in range(n)]

	for i in xrange(n):
		for j in xrange(i+1):
			if (i == 0) or (j == 0) or (i == j):
				pascal[i][j] = 1
			elif j == 1:
				pascal[i][j] = i
			else:
				pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
	return pascal[n-1][k-1] + pascal[n-1][k]

def binomial_bottomUp(n,k):
	pascal = [ [0]*(i+1) for i in range(n)]
	if n == 0 or k == 0 or n == k:
		return 1
	elif k == 1:
		return n

	if pascal[n-1][k-1] == 0:
		pascal[n-1][k-1] = binomial_bottomUp(n-1, k-1)
	if pascal[n-1][k] == 0:
		pascal[n-1][k] = binomial_bottomUp(n-1,k)
	return pascal[n-1][k-1] + pascal[n-1][k]

print binomial_bottomUp(5,4)