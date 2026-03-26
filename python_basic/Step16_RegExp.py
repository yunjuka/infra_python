# Step16_RegExp.py

'''
    정규표현식 (Regular Expression)
'''

import re

data:str = "apple, banana, cherry"

result = re.findall(r"a",data)

print(result)


text:str = "Contact: 010-1111-2222 입니다"

m_obj = re.search("010-[0-9]{4}-[0-9]{4}",text)

print(m_obj)
print(m_obj.group())