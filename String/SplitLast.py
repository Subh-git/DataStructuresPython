'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-12-01 11:30
	@Title : To get the last part of the string before a specified character.
	
'''
def split_last_specific(string,char):
    '''
    Description:
        This function splits the last part of the string before a specified character.
    Parameter:
        This takes the character and string as parameter.
    Return:
        This returns a s sliced string. 
    '''
    word =  string.rsplit(char,1)[0]
    return word



if __name__ == '__main__': 
    string = 'https://www.w3resource.com/python-exercises'
    char = '/'
    print(split_last_specific(string,char))
