'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-30 22:30
	@Title : To count the values associated with certain keys
	
'''
sample = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False,
         'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]

count = 0
for item in sample:
    if item['success'] == True:
        count+=1


print(count)