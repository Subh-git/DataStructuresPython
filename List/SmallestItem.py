'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-25 21:15
	@Title : To Find the smallest item in list
	
'''

list = [20,3,25,65,84,32,46,10,36]

def smallest(list):
    '''
    Description:
        This fucntion finds the smalles number from the list
    Parameter:
        This takes a list as argument.
    Return:
        Returns the smallest element
    '''
    #none is assigned so that we can compare it with any value
    small = None
    for i in list:
        if small is None:
            small = i
        if i < small:
            small = i
    return small

if __name__ == '__main__':
    try:
        print(list)
        print(smallest(list))
        print("Below is the smallest number checking using predefined method: min")
        print(min(list))
    except Exception as e:
        print(e)

