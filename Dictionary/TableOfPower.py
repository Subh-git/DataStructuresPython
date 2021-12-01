'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 20:35
	@Title : To generate and print a dictionary with (x,x*x)
	
'''


def generate_table(number):
    '''
    Description:
        This function creates a dictionary with key value pair in tables.
    Parameter:
        The number of entries.
    Returns:
        A dictionary
    '''
    count = 1
    dictionary = {}
    while count <= number:
        dictionary[count] = count*count
        count+=1

    return dictionary

if __name__ == '__main__':
    try:
        num = int(input("Please enter the number upto which iteration you want: "))
        print(generate_table(num))
    
    except ValueError:
        print("Invalid input")
