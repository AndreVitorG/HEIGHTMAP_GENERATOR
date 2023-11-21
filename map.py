import random


class Map:


	# generates the initial matrix of random integers from 0 to 300
	def create_matrix(self):

		height = 10
		width = 8

		# generates de matrix filled with 1's
		matrix = [[1 for _ in range(width + 1)] for _ in range(height)]

		# randomize the matrix content from 0 to 300
		for i in range(height):
			for j in range(width + 1):
				matrix[i][j] = random.randint(0, 300)

		return matrix

	# makes the matrix more readable and enumerates the rows and columns
	def process_matrix(matrix):

		alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
					'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '&', '*']

		# if the number is more than 100 turn it into 'III'
		# else if the number is less than 100 turn it into ' '
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j] < 100:
					matrix[i][j] = ' '
				else:
					matrix[i][j] = 'XXX'

		# enumerates the rows and columns (rows = numbers, columns  = letters)
		for i in range(len(matrix)):
			for j in range(len(matrix[0]) + 1):
				matrix[i][0] = len(matrix) - i - 1
				matrix[len(matrix) - 1][j - 1] = alphabet[j - 2]

		return matrix

	# prints the matrix in the screen, in a more readable way
	def print_matrix(matrix):
		# prints the matrix
		for i in matrix:
			print('\t'.join(map(str, i)))

#	def saves_matrix(matrix):

	# iterates all matrix values and adds a random number in between all cells
	def populate(matrix):
		aux2 = 0

		# creates the new rows to fit the new cells vertically and later horizontally
		for i in range(len(matrix) - 1):
			aux2 += 1
			matrix.insert(i + aux2, [])

		# VERTICAL - adds new cells in between old cells vertically
		# the new cell is a random number between it's above and below cell
		for k in range(len(matrix)):
			if (k % 2) != 0:
				for j in range(len(matrix[0])):
					if (k + 1) < (len(matrix)):
						a = matrix[k - 1][j]
						b = matrix[k + 1][j]
						if b > a:
							matrix[k].append((random.randint(a, b)))
						else:
							matrix[k].append((random.randint(b, a)))
			else:
				pass

		# updates the width to be used below
		width_ = (len(matrix[0])) - 1

		# HORIZONTAL - adds new cells in between old cells horizontally
		# the new cell is a random number between it's left and right cell
		for i in range(len(matrix)):
			aux = 0
			for j in range(width_):
				aux += 1
				a = matrix[i][j + aux - 1]
				b = matrix[i][j + aux]
				if b > a:
					matrix[i].insert(j + aux, random.randint(a, b))
				else:
					matrix[i].insert(j + aux, random.randint(b, a))

		return matrix
