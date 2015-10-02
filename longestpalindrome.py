'''
longestpalindrome.py
Frederik Roenn Stensaeth
09.27.15

A Python program to find the longest palindrome subsequence of a string.
Algorithm is implemented using dynamic programming.
'''

import sys
import time

def longestPalindrome(string):
	"""
	longestPalindrome() finds the longest palindrome subsequence of a given
	string using a table format.

	@params: string
	@return: string -> palindrome
	"""
	n = len(string)
	# Create table where we will keep the palindromes
	table = [['' for i in range(n)] for j in range(n)]

	# All strings of length 1 are palindromes
	for i in range(n):
		table[i][i] = string[i]

	# Sub_len is the length of the substring
	# We loop over all the possible sustring lengths.
	# Length 1 is not considered, as those were covered above.
	for sub_len in range(2, n + 1):
		# Need to find all the possible substrings of that length.
		# We do this by looping over all the possible starting indexes.
		for i in range(n - sub_len + 1):
			# Find the index at which the substring ends.
			j = i + sub_len - 1
			# Is the first and last letter the same? Length == 2?
			if string[i] == string[j] and sub_len == 2:
				# Palindrome contains two characters as the string is two
				# characters long.
				table[i][j] = string[i] + string[j]
			# Is the first and last letter the same?
			elif string[i] == string[j]:
				# Palindrome contains as many letters as the string that
				# did not contain the first and last letter we just compared
				# plus two, since we just found out that the first and last
				# letters are the same - so we need to add those.
				# As we have already found palindromes for all smaller strings
				# this is an easy look-up.
				table[i][j] = string[i] + table[i + 1][j - 1] + string[j]
			# First and last letters are not the same.
			elif sub_len == 2:
				table[i][j] = ''
			else:
				# Palindrome of this string is therefore the same length
				# as the one not containing either the first or the last
				# letter. So we need to find these. However, they have
				# already been found, so they are easy look-ups.
				if len(table[i][j - 1]) > len(table[i + 1][j]):
					table[i][j] = table[i][j - 1]
				else:
					table[i][j] = table[i + 1][j]

	return table[0][n - 1]

def main():
	if len(sys.argv) != 2:
		print('Error. Please provide a string to be checked for longest',
			  'palindrome.')
		print('Usage: $ python3 corrector.py <string>')
		sys.exit()
	palindrome = longestPalindrome(sys.argv[1])
	if palindrome == '':
		print('Longest palindrome for %s: <no palindrome>' % (sys.argv[1]))
	else:
		print('Longest palindrome for %s: %s' % 
			(sys.argv[1], longestPalindrome(sys.argv[1])))

	##### TESTS START
	# Tests written for timing the algorithm.
	# for j in range(10, 110, 10):
	# 	timeSTART = time.time()
	# 	table = longestPalindrome(sys.argv[1] * j)
	# 	timeSTOP = time.time()
	# 	print(timeSTOP - timeSTART)
	##### TESTS END

if __name__ == '__main__':
	main()


