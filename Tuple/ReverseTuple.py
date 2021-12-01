'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 13:10
	@Title : To reverse a given tuple
	
'''


def reverse_tup(tup):
    '''
    Description:
        This function reverses a given tuple.
    Parameter:
        This function takes a tuple.
    Return:
        A reversed element tuple.
    '''
    new_tup = ()
    #reversed is an in built function
    for k in reversed(tup):
        new_tup = new_tup + (k,)
    return new_tup



if __name__ == '__main__':
    try:
        tuple = ("Apple", "Mango", "Banana")
        print(tuple)
        print(reverse_tup(tuple))
    except Exception as e:
        print(e)
