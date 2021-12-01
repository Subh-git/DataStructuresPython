'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-12-01 10:55
	@Title : To sort in alphanumeric ways.
	
'''
string = "red, white, black, red, green, black"

def sort(string):
    '''
    Description:
        Takes a comma separated string and sorts them.
    Parameter:
        A string separated by comma.
    Return:
        The sorted string.
    '''
    word = set(string.split(','))
    string1 = str(",".join(sorted(word)))
    return string1


if __name__ == '__main__':  
    print(sort(string))
        
        