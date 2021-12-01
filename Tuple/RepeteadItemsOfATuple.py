'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 11:45
	@Title : To find the repeated item in tuple
	
'''

def check_rep(tup):
    '''
    Description:
        This function is used to find the repeated items in tuple.
    Parameter:
        This takes a tuple as a parameter.
    Return:
        It prints the repeated items and the number of repetitions.
    '''
    #the ref list is to avoid repeting the same print statement for multiple elements
    ref_list = []
    count=0
    for i in tup:
        if (tup.count(i)>1 and i not in ref_list):
            ref_list.append(i)
            print(i)
            print(f"The number of times {i} is repeated is: {tup.count(i)} ")
            count+=1

    if count < 1:
        print("There is no repetition")


if __name__ == '__main__':
    try:
        tuple = (10,20,10,30,45,10,20,45,10,78)
        print(tuple)
        check_rep(tuple)
    except Exception as e:
        print(e)