'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-26 11:00
	@Title : To check if there is atleast one common element in two given lists
	
'''

def check_comm(list1,list2):
    '''
    Description:
        This function checks if there is atleast a single common element in two list.
    Parameter:
        Two lists.
    Return:
        Returns true if common element found.
    '''
    for i in list1:
        if i not in list2:
            continue
        else:
            return True
    return False
    

if __name__ == '__main__':
    try:
        #defining and printing two lists
        list1 = ["Apple", "Mango", "Banana", "Watermelon"]
        list2 = ["Milshake", "Juice", "Apple", "Mango"]
        print(list1)
        print(list2)
        print(check_comm(list1,list2))

    except ValueError:
        print("Invalid Input")    
    except Exception as e:
        print(e)
