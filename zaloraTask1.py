def printNested(A):
	primitive = (int, float, complex, bool, str)
	for e in A:
		if isinstance(e, primitive):
			print e
		else:
			printNested(e)

import csv
def countAndSort():
	with open(raw_input()) as csvfile:
		reader = csv.reader(csvfile, delimiter=',',quotechar=None)
		chars = ['[','"',']']
		for line in reader:
			line[0] = line[0].replace('"[','')
			line[-1] = line[-1].replace(']"','')
			print line
			break
countAndSort()
