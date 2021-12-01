'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 15:30
	@Title : To add members in a set
	
'''

new_set = set()
n = 1
try:
    num = int(input("Please enter how many values u want to add: "))

    while n <= num:
        try:
            val = input(f"Please enter your {n} value: ")
            new_set.add(val)

        except ValueError:
            print("Invalid input")
        
        n+=1

except Exception as e:
    print(e)

print(new_set)
