'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-12-01 09:40
	@Title : To change the occurence of all the occurences of the first char leaving the first char itself
	
'''

def replace_all(string,val):
    '''
    Description:
        This function replaces all the occurence of the first letter of the string with given value leaving the first letter intact.
    Parameter:
        The string and the replacing value.
    Returns:
        The modified string.
    '''
    string1 = string[0]   #to get the first occurence.
    string = string.replace(string1,val)
    string2 = string1 + string[1:]
    return string2



if __name__ == '__main__':
    try:
        str = input("Please enter the string: ")
        value = input("Please enter the replacing value: ")
        print(replace_all(str,value))
    
    except Exception as e:
        print(e)