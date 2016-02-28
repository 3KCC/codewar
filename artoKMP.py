#inputs: n = length of text, T = the text
#outputs: the list (pi) of length (int) of longest substring that is both prefix and suffix at each position start at 1
#define pi[0] = -1
def piArr(n, T):
	pi = [0]*(n+1)
	pi[0] = -1
	pi[1] = 0
	for i in xrange(2,n+1):
		k = pi[i-1]
		while k > 0 and T[k] != T[i-1]:
			k = pi[k]
		if T[k] == T[i-1]:
			pi[i] = k + 1

	return pi

#inputs: l = the length of pattern, P = the pattern, T = the text
#output: print out the position where matches found
def kmpSearch(l, P, T):
	i = 0
	N = len(T)
	pi = piArr(l, P)
	if l <= N:
		while i < N:
			k = 0
			j = i
			while k < l and j < N and T[j] == P[k]:
				k += 1
				j += 1
			if k == l:
				print i
			i += (k - pi[k])
		

# f = open('input.txt')
# txt = f.readline().strip()
# while txt != '':
# 	case = []
# 	for k in xrange(3):
# 		case.append(txt)
# 		txt = f.readline().strip()
# 	length = int(case[0])
# 	neddle = case[1]
# 	haystack = case[2]
# 	kmpSearch(length,neddle,haystack)
# 	print ''



# def main():
# 	while True:
# 		length = raw_input()
# 		if length:
# 			length = int(length)
# 			neddle = raw_input()
# 			haystack = raw_input()
# 			kmpSearch(length,neddle,haystack)
# 			print ''
# 		else:
# 			break



# def main():
# 	inputArr = []
# 	while True:
# 		inp = raw_input()
# 		if inp:
# 			length = int(inp)
# 			needle = raw_input()
# 			haystack = raw_input()
# 			inputArr.append([length, needle, haystack])
# 		else:
# 			break
# 	for e in inputArr:
# 		kmpSearch(e[0], e[1], e[2])
# 		print ''

import sys
def main():
	for txt in sys.stdin.readline().strip():
		# txt = f.readline().strip()
		cases = []
		while txt != '':
			case = []
			for k in xrange(3):
				case.append(txt)
				txt = sys.stdin.readline().strip()
			cases.append(case)
		for case in cases:
			length = int(case[0])
			neddle = case[1]
			haystack = case[2]
			kmpSearch(length,neddle,haystack)
			print ''


if __name__ == "__main__":
	main()