'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 16:00
	@Title : To remove elements from a set if it is present
	
'''

new_set = {"Apple", "Cherry", "Tomatoes", "Avocado", "Watermelon"}

try:
    print(new_set)
    val = input("Please enter the value you want to remove: ")
    new_set.remove(val)
    print(new_set)

except Exception as e:
    print(e)