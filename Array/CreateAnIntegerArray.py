'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-25 19:00
	@Title : Array creation and visualisatiaon
	
'''

import array as arr

num_arr = arr.array('i',[10,20,30,40,50] )

for element in num_arr:
    print(element,end= " ")

#let user describe the index which he want to choose
try:
    index = len(num_arr)-1
    opt =  int(input(f"\n Please select the index ranging from 0 to {index}: "))
    x = num_arr[opt]
    print(f"The number in index {opt} is: {x}")

except ValueError as e:
    print("Invalid input",e)

except IndexError as e:
    print(e)

