'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 16:00
	@Title : To make an intersection of two sets
	
'''

set1 = {"Orange", "Lemon", "Tomato", "Brinjal"}
set2 = {"Lemon", "Tomato","Ginger", "Tea"}

print("Original sets are as follows:--- \n")
print(set1)
print(set2)

print("\n After intersection---- \n ")
#set3 = set1 & set2   -1st way
set3 = set1.intersection(set2)      #2nd - way
print(set3)
