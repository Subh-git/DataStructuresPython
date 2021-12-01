'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-26 16:00
	@Title : To check the circular identicality of two lists
	
'''

def circular_identical(list1,list2):
    '''
    Description:
        This fucntion checks whether two lists are circularly identical or not.
    Parameter:
        Two lists.
    Return:
        yes or no depending upon circularly identical
    '''
    if len(list1) != len(list2):
        return False
    
    #doubling is necessary to check for every value upto the end index of list2
    return (' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))

if __name__ == '__main__':
    try:
        
        list1 = [10,10,10,0,0]
        list2 = [0,0,10,10,10]
        print(list1)
        print(list2)
        print("\n Circular check---")
        print(circular_identical(list1,list2))
   
    except Exception as e:
        print(e)