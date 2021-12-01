'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 18:00
	@Title : To create a frozen set
	
'''
set1 = {"Orange", "Lemon", "Tomato", "Brinjal"}
set2 = {"Lemon", "Tomato","Ginger", "Tea"}

#frozen sets take iterable objects and make them immutable, it doesnt let us use remove or discard option
set_frozen1 = frozenset(set1)
set_frozen2 = frozenset(set2)

print("The frozen sets are: ")
print(set_frozen1)
print(set_frozen2)

print("The differnce between the two sets are: ", set_frozen1-set_frozen2)
print("The union of two sets are: ", set_frozen1.union(set_frozen2))

