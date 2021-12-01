'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-26 11:00
	@Title : To remove duplicate elements from the list
	
'''
list = ["Apple", "Mango", "Pears", "Apple", "Mango", "Banana", "Water Melon"]

def remove_dup(list):
    '''
    Description:
        This fucntion removes duplicate entries from the list
    Parameter:
        This takes a list as argument.
    Return:
        Returns a Unique list
    '''
    lst = []
    for i in list:
        if i not in lst:
            lst.append(i)

    return lst

if __name__ == '__main__':
    try:
        print(list)
        print("\n After removing duplicates----- \n")
        print(remove_dup(list))
    except Exception as e:
        print(e)
