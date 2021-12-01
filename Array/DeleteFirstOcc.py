'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-25 20:00
	@Title : To remove the first occurence of the specified array element
	
'''

import array as arr


num_arr = arr.array('i',[10,20,30,40,50,10,10,20,56,30,10,50,30] )
for element in num_arr:
    print(element,end= " ")

#remove deletes the first occurence of the element
try:
	num = int(input("\n Please enter the number whoose first occurence you want to remove: "))
	num_arr.remove(num)

except ValueError as e:
	print("Invalid input",e)
except Exception as e:
	print(e)

for element in num_arr:
    print(element,end= " ")