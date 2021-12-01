'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 19:50
	@Title : To concatenate dictionaries
	
'''
def concatenate(dic1,dic2):
    '''
    Description:
        This function takes two dictionaries and merges them.
    Parameter:
        Two dictionaries.
    Returns:
        A merged Dictionary. 
    '''
    #These two methods can be used
    #The dic1| dic2 is available from python 9 and upwards. update changes the dictonary and doesn't return a new dictionary. 
    dic1.update(dic2)
    #res = dic1 | dic2
    return dic1


if __name__ == '__main__':
    try:
        dic1={1:10, 2:20}
        dic2={3:30, 4:40}
        dic3={5:50,6:60}

        print("Before concatenation----- \n")
        print(dic1)
        print(dic2)
        print(dic3)

        print("\n After concatenation of the 3--- \n")

        res = concatenate(dic1,dic2)
        print(concatenate(res,dic3))

    except Exception as e:
        print(e)