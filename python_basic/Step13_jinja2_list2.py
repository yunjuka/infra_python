# Step13_jinja2_list2.py

# 게시글 목록이 담긴 리스트

from jinja2 import Template


posts:list = [
    {"id":1, "writer":"작성자1", "title":"제목1"},
    {"id":2, "writer":"작성자2", "title":"제목2"},
    {"id":3, "writer":"작성자3", "title":"제목3"},
]

'''
    위의 posts 에 담긴 데이터를 이용해서 아래와 같이 출력되도록

    글 목록 입니다.
    - 글번호: 1, 작성자: 작성자1, 제목: 제목1

'''

lists_template:str = '''
    글 목록 입니다.
    {% for post in posts %}
    - 글 번호: {{post.id}}, 작성자: {{post.writer}}, 제목: {{post.title}}
    {% endfor %}
'''

temp:Template = Template(lists_template)

result:str = temp.render(posts=posts)
print(result)