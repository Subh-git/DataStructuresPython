'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 12:35
	@Title : To remove an item from a tuple
	
'''

tup = (10,20,30,40,50)
print(tup)
#tuple doesnt allow deletetion directly so we convert first to a list and then perform the operation.
new_list = list(tup)
new_list.remove(30)      #removing 30 from the list
tup = tuple(new_list)
print(tup)