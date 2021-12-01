'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 21:30
	@Title : To convert a list into a nested dictionary of keys.
	
'''

num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)