import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	test = test.replace('\n','').split(';')
	numRows = int(test[0])
	numCols = int(test[1])
	list = test[2].split(' ')
	solution = ''
	size = 0
	n = 0
	
	while size < numRows * numCols:
		# Top, from left to right
		for i in range(n,numCols-n):
			if i > 0 or n > 0:
				solution += ' '
			solution += list[i + n*numCols]
			size += 1
		
		if size >= numRows * numCols:
			break
		
		# Right, from top to bottom
		for i in range (n+1, numRows-n):
			solution += ' ' + list[i*numCols + numCols - 1 - n]
			size += 1
		
		if size >= numRows * numCols:
			break
		
		# Bottom, from right to left
		for i in range(n, numCols-n-1):
			solution += ' ' + list[numCols*(numRows-n) - 2 - i]
			size += 1
		
		if size >= numRows * numCols:
			break
		
		# Left, from bottom to top
		for i in range(n, numRows-n-2):
			solution += ' ' + list[numCols*(numRows-2-i)+n]
			size += 1
		
		if size >= numRows * numCols:
			break
		
		n += 1
	
	print solution

test_cases.close()
