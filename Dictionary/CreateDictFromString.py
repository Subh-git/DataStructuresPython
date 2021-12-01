'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 21:30
	@Title : To create a dictionary with a given string
	
'''
def str_frequency(str):
    '''
    Description:
        This function creates a frequency distribution of the string.
    Parameter:
        This takes a string as parameter.
    Return:
        A dictionary
    '''
    dictionary = {}
    for word in str:
        dictionary[word] = dictionary.get(word,0)+1
    
    return dictionary



if __name__ == '__main__':
    try:
        string = input("Please enter your string: ")
        print(str_frequency(string))
    
    except Exception as e:
        print(e)
