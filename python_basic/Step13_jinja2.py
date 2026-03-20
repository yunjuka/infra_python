# Step13_jinja2.py

# 테스트용 template

from jinja2 import Template


my_template  = """
    번호 : {{ num }}
    이름 : {{ name }}
    주소 : {{ addr }}
"""

# templeate에 출력할 데이터 준비
mem1 = {"num":1, "name":"김구라", "addr":"노량진"}
mem2 = {"num":2, "name":"해골", "addr":"행신동"}

temp:Template = Template(my_template)
result1 = temp.render(mem1)
print(result1)

result2 = temp.render(mem2)
print(result2)