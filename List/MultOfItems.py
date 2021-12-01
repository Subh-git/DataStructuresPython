'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-25 20:45
	@Title : To multiply all the items of a list
	
'''

list = [5,10,15,3,45]

def mult_items(list):
    '''
    Description:
        This fucntion multiplies the elements of an integer/float list.
    Parameter:
        This takes a list as argument.
    Return:
        Returns the multiplied value of all the elements
    '''
    product = 1
    for i in list:
        product = i*product
    return product


if __name__ == '__main__':
    print(list)
    print(mult_items(list))