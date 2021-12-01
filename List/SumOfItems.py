'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-25 20:30
	@Title : To sum the items of a list
	
'''


list1 = [10,20,30,40,50]

def add_items(list):
    '''
    Description:
        This fucntion adds the elements of an integer/float list.
    Parameter:
        This takes a list as argument.
    Return:
        Returns the total of all the elements
    '''
    sum = 0
    for i in list:
        sum = sum + i
    return sum

if __name__ == '__main__':
    print(list1)
    print(add_items(list1))

