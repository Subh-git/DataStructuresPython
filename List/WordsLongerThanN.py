'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-26 11:10
	@Title : To create a list of words longer than a number N
	
'''

#random user defined list of words
list = ["Rahul","abc", "xyz", "Subha", "Mango", "Building","Jamshedpur", "To", "Rockford Lane"]

def create_list(val,list):
    '''
    Description:
        This function creates a list out of the given list whoose length of words are greater than the number provided by the user
    Parameter:
        The length of word to be formed and the list
    Return:
        A new list
    
    '''
    new_list = []
    for i in list:
        if len(i) > val:
            if i not in new_list:
                new_list.append(i)
    
    if len(new_list) == 0:
        return "There is no such word"
    
    return new_list

if __name__ == '__main__':
    try:
        print("This is the list that you have---")
        print(list)
        num = int(input("Please enter the minimum word length above which you want the words to be in list: "))
        a = create_list(num,list)
        print(a)
        
    except ValueError:
        print("Invalid Input")    
    except Exception as e:
        print(e)
