'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 20:55
	@Title : To show unique values in dictionary
	
'''
def print_unique(list):
    '''
    Description:
        This function takes a list and prints out the unique values inside the dictionaries.
    Parameter:
        This takes a list as parameter.
    Returns:
        Returns a unique valued set.
    '''
    #we declare a set as set is immutable as well as it is unique
    new_set = set()
    for item in list:
        for k,v in item.items():
            new_set.add(v)
    
    return new_set

if __name__ == '__main__':
    try:
        sample = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
        print(print_unique(sample))
    except Exception as e:
        print(e)
