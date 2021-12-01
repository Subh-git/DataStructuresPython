'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 19:30
	@Title : To sort a dictionary by value
	
'''

new_dict = {"Apple": 20, "Orange" : 15, "Sugar": 25, "Green":34}
print(new_dict)
#sorted function takes any iterable element and always returns a list
#For arranging in descending order by value
print(dict(sorted(new_dict.items(), key = lambda k: k[1], reverse= True)))
#For arranging in ascending order by value
print(dict(sorted(new_dict.items(), key = lambda k: k[1])))
