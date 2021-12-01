'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-26 19:20
	@Title : To remove duplicates from a list of lists
	
'''

def remove_duplicates(list):
    '''
    Description:
        This fucntion removes duplicate entries from the list
    Parameter:
        This takes a list as argument.
    Return:
        Returns a Unique list
    '''
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list


if __name__ == '__main__':
    try:
        list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
        print(list)
        print("\n After removing duplicates----- \n")
        print(remove_duplicates(list))
    except Exception as e:
        print(e)
