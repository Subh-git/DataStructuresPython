'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-26 15:20
	@Title : To append a list in another list
	
'''

def append(list1, list2):
    '''
    Description:
        This function appends a list in another list.
    Parameter:
        Takes teo lists.
    Return:
        Returns a combined list.
    '''
    lst = []
    lst = list1 + list2
    return lst

if __name__ == '__main__':
    try:
        
        list1 = ["Apple", "Mango", "Banana", "Watermelon"]
        list2 = ["Milshake", "Juice", "Apple", "Mango"]
        print(list1)
        print(list2)
        print("\n Below is the resultant list after appending both------ \n")
        print(append(list1,list2))
   
    except Exception as e:
        print(e)
