'''Solution is quite simple:
	1. generate matrices with  produts of elements in each column in three directions;
	2. find index of max element in these matrices. 
'''

import numpy as np

size = 10
matrix = np.random.randint(0, 10, (size, size, size))

#list that stores tuple with indexis in each direction
index = []

for i in range(3):
	#matrix with  produts of elements in  each column by i-th axis
	prodMatrix = np.prod(matrix, axis = i)

	flatten_index = np.argmin(prodMatrix)
	#argmin returns index in flatten array,
	#so we need to convert it to 3d indices 
	indices = np.unravel_index(flatten_index, prodMatrix.shape)
	index.append(indices)


print(matrix[ :, index[0][0], index[0][1]])
print(matrix[index[1][0], :, index[1][1]])
print(matrix[index[2][0], index[2][1], :])


