def main():

	str1 = input('Text 1: ')
	str2 = input('Text 2: ')

	M = len(str1)
	N = len(str2)

	# Initialize matrix
	D = [ [ 0 for j in range(N) ] for i in range(M) ]

	for i in range(M):
		D[i][0] = i

	for j in range(N):
		D[0][j] = j

	# Calculate distance
	for i in range(M):
		for j in range(N):

			D[i][j] = min( 
							D[i-1][j] + 1,
							D[i][j-1]+1,
							D[i-1][j-1] + (
								2 if str1[i] != str2[j] else 0
								)
							)

			pass

		pass

	print("\nDistance between \"%s\" and \"%s\": %d" % (str1, str2, D[M-1][N-1]))

	pass

if __name__ == '__main__':
	main()