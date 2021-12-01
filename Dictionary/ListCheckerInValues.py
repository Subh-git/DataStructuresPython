'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-12-01 00:30
	@Title : To Count the number of items in list which are values in a dictionary.

'''

def count_list_items(dict):
    '''
    Description:
        This fucntion takes a dictionary and then checks if the values of the dictionary conatains list.
    Parameter:
        A dictionary.
    Return:
        The count of items in the list. 
    '''
    count = 0
    for k,v in dict.items():
        if isinstance(v, list):
            count+= len(v)
    
    return count


if __name__ == '__main__':
    try:
        sample = { 'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'B' : 34,
        'C' : 12,
        'D' : [7, 8, 9, 6, 4] }

        print(count_list_items(sample))
    except Exception as e:
        print(e)