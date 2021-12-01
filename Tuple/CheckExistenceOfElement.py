'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 12:30
	@Title : To check if an element exist in the tuple
	
'''
def check(tup,value):
    '''
    Description:
        This function checks whther the input is present in the tuple or not.
    Parameter:
        This function takes a tuple and the value as a parameter.
    Returns:
        True or False.
    '''

    if value in tup:
        return True
    else:
        return False


if __name__ == '__main__':
    try:
        tuple = (10,20,10,30,45,10,20,45,10,78)
        print(tuple)
        val = int(input("Please enter the value you want to check in the tuple. "))
        print(check(tuple,val))

    except ValueError:
        print("Invalid input type")
    except Exception as e:
        print(e)