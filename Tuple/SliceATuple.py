'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 12:45
	@Title : To slice a tuple
	
'''
tup = (10,20,30,40,50,60,70)

try:
    print(tup)
    num1 = int(input("Please enter the starting index: "))
    num2 = int(input("Please enter the index upto which you want to slice: "))
    num3 = int(input("Please enter the step of slicing: "))
    if num3 == 0:
        print(tup[num1:num2])
    else:
        print(tup[num1:num2:num3])
except ValueError:
    print("Invalid input")
except Exception as e:
    print(e)
