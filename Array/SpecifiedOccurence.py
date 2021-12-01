'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-25 20:00
	@Title : To check the occurence of a specified item in an array
	
'''

import array as arr

num_arr = arr.array('i',[10,20,30,40,50,10,10,20,56,30,10,50,30] )

def count_occurence(val,arr):
    '''
    Description: 
        This fucntion counts the occurence of the specified item in an array.
    Parameter:
        The item and the array.
    Return:
        The number of occurence of the item in the array
    '''
    count = 0
    for element in arr:
        if element == val:
            count+=1
        else:
            pass
    return count

#Entry point
if __name__ == '__main__':
    
    for i in num_arr:
        print(i, end=" ")
    try:
        value = int(input("\n Please enter the value whose occurence you want to check: "))
        print(count_occurence(value,num_arr))
    
    except ValueError as e:
        print("Invalid input",e)
    except Exception as e:
        print(e)
