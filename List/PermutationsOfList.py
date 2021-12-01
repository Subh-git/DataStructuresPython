'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-26 15:00
	@Title : To generate all permutauions of a given list
	
'''

# itertools is a module that contains the permutation in buil functions
import itertools

lst = [1,2,3]

print(list(itertools.permutations(lst)))
#itertools. permutauions generates a permutauion object which can be converted to list data type and then printed