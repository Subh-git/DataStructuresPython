'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 20:45
	@Title : To remove a key from a dictionary
	
'''
new_dict = {"Apple": 20, "Orange" : 15, "Sugar": 25, "Green":34}
print(new_dict)
#using pop
new_dict.pop("Apple")
print(new_dict)
#using del keyword. del generates an exception if key doesn't exist
del new_dict["Orange"]
print(new_dict)