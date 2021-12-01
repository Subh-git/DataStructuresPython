'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-25 19:25
	@Title : Reversing the array elements
	
'''

import array as arr

num_arr = arr.array('i',[10,20,30,40,50] )

print("Before reversing")

for element in num_arr:
    print(element,end= " ")
    
#using the inbuilt reverse fuction
num_arr.reverse()

print("\n After reversing.")

for element in num_arr:
    print(element,end= " ")


