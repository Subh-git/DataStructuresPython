'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 23:30
	@Title : To check the existence of multiple keys
	
'''

new_dict = {"Apple": 20, "Orange" : 15, "Sugar": 25, "Green":34}

print(new_dict.keys() >= {"Apple", "Orange"})
print(new_dict.keys() >= {"Apple", "White"})
print(new_dict.keys() >= {"Apple", "Orange", "Sugar"})