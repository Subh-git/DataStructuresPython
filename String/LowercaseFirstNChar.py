'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-12-01 12:45
	@Title : To lowercase first N characters of a string.
	
'''

def lower_first(string,n):
    '''
    Description:
        This takes the string and the lowercases the first n characters of the string.
    Parameter:
        This takes the string and the input n.
    Return:
        The modified string.
    '''
    try:
        str = string[:n].lower()
        return (str + string[n:]) 

    except Exception as e:
        print(e)

    

if __name__ == '__main__':
    try:
        str = input("Please enter the string: ")
        value = int(input("Please enter the index number upto which you want lowercase: "))
        print(lower_first(str,value))
    
    except Exception as e:
        print(e)   