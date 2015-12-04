#O(n^2)
def selectionSort(A):
	n = len(A)
	for k in xrange(n):
		minimum = k
		for j in xrange(k+1,n):
			if A[j] < A[minimum]:
				minimum = j
		A[k], A[minimum] = A[minimum], A[k]
	return A

#O(n+k)
#Only valid when range of sorted values in 0..k
def countingSort(A, k):
	n = len(A)
	count = [0]*(k+1)
	for i in xrange(n):
		count[A[i]] += 1
	p = 0
	for i in xrange(i+1):
		for j in xrange(count[i]):
			A[p] = i
			p += 1
	return A

def mergeSort(A):
    if len(A)>1:
        mid = len(A)//2
        lefthalf = A[:mid]
        righthalf = A[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i= j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                A[k]=lefthalf[i]
                i=i+1
            else:
                A[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            A[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            A[k]=righthalf[j]
            j=j+1
            k=k+1
    return A


print mergeSort(input())
#print countingSort(input(),input())
#print selectionSort(input())
