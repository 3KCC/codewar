f = open('properBrackets.txt')
T = int(f.readline().strip())
boards = []
for i in xrange(T):
	boards.append(f.readline().strip().split())
print boards