'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 22:00
	@Title : To print the dictionary in table format
	
'''
dict1 = {1: ["Samuel", 21, 'Data Structures'],
     2: ["Richie", 20, 'Machine Learning'],
     3: ["Lauren", 21, 'OOPS with java'],
     }
print ("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))

for key, value in dict1.items():
    name, age, course = value      #unpacking
    print ("{:<10} {:<10} {:<10}".format(name, age, course))
