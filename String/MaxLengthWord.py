'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-12-01 10:30
	@Title : To obtain the length of the longest word from the list
	
'''

def longest(list):
    '''
    Description:
        The fucntion returns the length of the longest word from the list of words.
    Parameter:
        This takes a list as input.
    Returns:
        This returns the length of the word.
    '''
    count = 0
    for i in list:
        if len(i) > count:
            count = len(i)
        
    return count



if __name__ == '__main__':
    lst = ["Subhadeep", "Rahul", "Animesh", "Subham", "Dev"]
    print(longest(lst))