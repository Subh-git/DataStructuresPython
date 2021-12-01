'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-26 10:00
	@Title : To sort the entry by the last element of the tuple element in list
	
'''

list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def sort_second(list):
    '''
    Description:
        This function just sorts the list in ascending order according to the last element of the tuple element.
    Parameter:
        The list as the parameter.
    Return:
        The sorted list.
    '''

    #we are using the bubble sort algorithm
    lst = len(list)
    #The in range iterates from 0 to 4
    for i in range(lst):
        #j is the tuple element and its range is like 0,1,2, then it decreases 0,1
        for j in range(lst -i - 1):
            #storing temporary variable with the element using indexing
            if(list[j][1] > list[j+1][1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1]= temp
    
    return list

    #another method that can be implemented is using lambda
    #list.sort(key = lambda x: x[1])
    #return list
       

if __name__ == '__main__':
    try:
        print(list)
        print("After sorting-----")
        sort_second(list)
        print(list)
    except Exception as e:
        print(e)