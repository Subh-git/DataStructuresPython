'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-26 19:00
	@Title : To find common items in two lists
	
'''


def common_items(list1,list2):
    '''
    Description:
        This function returns a list with all the common items in given two lists.
    Parameter:
        Two lists.
    Return:
        A list with all the common elements.
    '''
    comm = []
    for i in list1:
        if i in list2 and i not in comm:
            comm.append(i)

    if len(comm) == 0:
        return "No common elements "

    else:
        return comm

if __name__ == '__main__':
    try:
        
        list1 = ["Apple", "Mango", "Pears", "Guava","Apple"]
        list2 = ["Watermelon", "Muskmelon", "Guava", "Apple"]
        print(list1)
        print(list2)
        print("\n Common--- \n")
        print(common_items(list1,list2))
   
    except Exception as e:
        print(e)