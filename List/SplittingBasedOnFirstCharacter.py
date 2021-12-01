'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-26 17:00
	@Title : To split a given list based on first character of word
	
'''

def split_list(list):
    '''
    Description:
        The following function takes a list and splits it on the basis of the first character of the word.
    Paramter:
        A list.
    Return:
        Prints the list items.
    '''
    a_list = []
    for i in range(len(list)):
        words = list[i]
        letter = words[0]
        #the below block is to avoid repetrion of the same letter twice
        if letter not in a_list:
            a_list.append(letter)
            print(letter)

            #The below block is to iterate and print the words that matches with the first character of the word
            for j in list:
                if j.startswith(letter):
                    print(j)
            print("---------------")
    
if __name__ == '__main__':
    try:
        lst = ["Apple", "Aam", "Mango", "Balloon"]
        split_list(lst)
    except Exception as e:
        print(e)
