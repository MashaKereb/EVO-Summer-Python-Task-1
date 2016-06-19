'''Solution is quite simple:
	1. generate matrices with sum of elements in each column in three directions;
	2. find index of max element in these matrices. 
'''

import numpy as np

def getIndexOfMax(matrix, axis):
	'''Returns the index of column with maximum sum of numbers 
	in one of three directions
	'''
	sumMatrix = np.sum(matrix, axis=axis)

	index = np.argmax(sumMatrix)

	#np.argmax returns two-digit integer, that represents
	#row and column number. So, we need to translate it into a tuple
	return index/10, index%10

size = 10
matrix = np.random.randint(0, 10, (size, size, size))

index = [getIndexOfMax(matrix, i) for i in range(3)]

print([matrix[ i, index[0][0], index[0][1]] for i in range(size)])
print([matrix[index[1][0], i, index[1][1]] for i in range(size)])
print([matrix[index[2][0], index[2][1], i] for i in range(size)])


