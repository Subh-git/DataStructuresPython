'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-25 21:30
	@Title : To Count the strings whose ending and begining are same and contains atleast 2 characters
	
'''

list = ['abc','xyz','1221','aba']

def count_string(list):
    '''
    Description:
        This fucntion finds the count of string items whoose first and last character are same and the length of individual string is 
        more than 2
    Parameter:
        This takes a list as argument.
    Return:
        Returns the count of strings satisfying the condition
    '''
    count = 0
    for item in list:
        if len(item) >= 2:
            #getting the 1st element from the string
            a = item[0]
            #getting the last element from the string
            b = item[len(item)-1]
            if a == b:
                count+= 1
    return count

if __name__ == '__main__':
    try:
        print(list)
        print(count_string(list))

    except Exception as e:
        print(e)

