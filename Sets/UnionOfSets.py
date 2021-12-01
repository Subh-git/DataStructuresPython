'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 16:10
	@Title : To create a union of two sets
	
'''


set1 = {"Orange", "Lemon", "Tomato", "Brinjal"}
set2 = {"Lemon", "Tomato","Ginger", "Tea"}

print("Original sets are as follows:--- \n")
print(set1)
print(set2)

print("\n After union---- \n ")
set3 = set1.union(set2)
print(set3)