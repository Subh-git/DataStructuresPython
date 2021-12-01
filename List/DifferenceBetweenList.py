'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-26 15:10
	@Title : To get the difference between two lists
	
'''

list1 = [10,20,30,40,50]
list2= [20,45,60,30]
#the difference between these two lists should yield 10,40,50,45,60

def differene_list(list1,list2):
    '''
    Description:
        The following function gets the different elements in two lists
    Parameter:
        This function  takes two lists as arguments
    Return:
        A list with all the different elements
    '''
    diff = []
    #checking elements in list1
    for i in list1:
        if i not in list2:
            diff.append(i)
    #checking elements in list2
    for j in list2:
        if j not in (list1 or diff):
            diff.append(j)

    return diff

if __name__ == '__main__':
    print(differene_list(list1,list2))