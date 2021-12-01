'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 17:00
	@Title : To create a symmetric differnce of two sets
	
'''
set1 = {"Orange", "Lemon", "Tomato", "Brinjal"}
set2 = {"Lemon", "Tomato","Ginger", "Tea"}

print("Original sets are as follows:--- \n")
print(set1)
print(set2)

print("\n The symmetric differnce between set1 and set2 \n")
print(set1.symmetric_difference(set2))
