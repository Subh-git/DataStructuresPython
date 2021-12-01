'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 10:10
	@Title : To unpack a tuple in various variables
	
'''
if __name__ == '__main__':
    try:
        tup = ("Roses","Marigold", "Flowers", "Daffodil")
        x,y,z,w = tup
        print(x)
        print(y)
        print(z)
        print(w)
        print()

        #in the below code we have used the string *args packing which means multiple values can be unpacked in a single variable
        x,*y,w = tup
        print(x)
        print(y)
        print(z)

    except Exception as e:
        print(e)

