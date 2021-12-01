'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-12-01 12:00
	@Title : To format the string with width = 50
	
'''

import textwrap
sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
print()
print(textwrap.fill(sample_text, width=50))
print()
