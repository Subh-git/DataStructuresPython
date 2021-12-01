'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-26 18:00
	@Title : To remove specific elements at given indexes
	
'''
#user defined list
list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

def remove_pos(list):
    '''
    Description:
        This function removes certain elements from the list at 0, 4 and 5 index.
    Parameter:
        The list.
    Return:
        Returns the new list with items removed.
    '''
    #it is always advisable to delete the largest index first so that other indexes does'nt change
    del list[5]
    del list[4]
    del list[0]
    return list


if __name__ == '__main__':
    try:
        print(list)
        print(remove_pos(list))
  
    except Exception as e:
        print(e)

