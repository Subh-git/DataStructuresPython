'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-12-01 10:00
	@Title : To add ing or ly at the end.
	
'''

def add_ing(string):
    '''
    Description:
        This function adds an ing or ly at the end of the string.
    Parameter:
        The string.
    Returns:
        The modified string.
    '''
    if len(string) < 3:
        return "Length less than 3!"
    
    str = string[(len(string)-3):]
    if str == 'ing':
        string = string+'ly'
    else:
         string = string+'ing'
    
    return string



if __name__ == '__main__':
    try:
        str = input("Please enter the string: ")
        print(add_ing(str))
    
    except Exception as e:
        print(e)