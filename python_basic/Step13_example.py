# Step13_example.py

from jinja2 import Template

info:dict = {
    "num":1,
    "name":"김구라",
    "body":{
        "height": 180,
        "weight": 80
    },
    "hobby": ["피아노", "당구", "프로그래밍"]
}

info_template:str = '''
    번호: {{info.num}}
    이름: {{info.name}}
    키: {{info.body.height}} cm
    몸무게: {{info.body.weight}} kg
    취미: 
    {% for i in info.hobby %}
        - {{i}}
    {% endfor %}
'''

temp:Template = Template(info_template)

result:str = temp.render(info=info)
print(result)