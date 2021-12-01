'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 16:15
	@Title : To create a differnce of two sets
	
'''

set1 = {"Orange", "Lemon", "Tomato", "Brinjal"}
set2 = {"Lemon", "Tomato","Ginger", "Tea"}
set3 = {"Tea", "Orange", "Cake", "Avocado"}

print("Original sets are as follows:--- \n")
print(set1)
print(set2)
print(set3)

print("\n The differnce between set1 - set2 \n")
print(set1.difference(set2))
print("\n The differnce between set2 - set1 \n")
print(set2 - set1)
print("\n The differnce between set3 - set2,set1 \n")
print(set3.difference(set1,set2))
