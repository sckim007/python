'''
1. JSON
JSON은 JavaScript Object Notation의 약자로서 JavaScript 문법에 영향을 받아 개발된 Lightweight한 데이타 표현 방식이다.
JSON은 데이타를 교환하는 한 포맷으로서 그 단순함과 유연함 때문에 널리 사용되고 있다. 특히 웹 브라우져와 웹서버 사이에
데이타를 교환하는데 많이 사용되고 있다. 가장 많이 사용되는 JSON 포맷은 Key-Value Pair의 컬렉션이다.

Python은 기본적으로 JSON 표준 라이브러리(json)를 제공하고 있는데, "import json" 을 사용하여 JSON 라이브러리를 사용할 수
있다 (주: Python 2.6 이상).
JSON 라이브러리를 사용하면, Python 타입의 Object를 JSON 문자열로 변경할 수 있으며(JSON 인코딩), 또한 JSON 문자열을 다시
Python 타입으로 변환할 수 있다 (JSON 디코딩).
'''

'''
2. JSON 인코딩
Python Object (Dictionary, List, Tuple 등) 를 JSON 문자열로 변경하는 것을 JSON Encoding 이라 부른다. JSON 인코딩을
위해서는 우선 json 라이브러리를 import 한 후, json.dumps() 메서드를 써서 Python Object를 문자열로 변환하면 된다.

예를 들어, 아래 코드는 customer 라는 Python Dictionary 객체를 JSON 문자열로 인코딩하는 예이다.
결과물 jsonString은 JSON 표현을 갖는 문자열(str 타입)이다.
'''
import json

# 테스트용 JSON Dictionary
customer = {
    'id': 721112,
    'name': '김선철',
    'history': [
        {'date': '2015-03-11', 'item': 'iPhone'},
        {'date': '2016-02-23', 'item': 'Monitor'}
    ]
}

# JSON 인코딩
jsonString = json.dumps(customer)

# 문자열 출력
print(jsonString)
print(type(jsonString))

'''
위의 코드를 실행하면 JSON 문자열이 한 줄로 길게 표현됨을 알 수 있다. 이렇게 축약된 JSON 문자열은 다른 컴퓨터나 
네트워크 상에 보낼 때 유용하지만, 화면에 표시할 필요가 있을 경우는 읽기가 불편하다. 
JSON 문자열을 읽기 편하게 할 필요가 있을 경우에는, 아래와 같이 "indent" 옵션을 json.dumps() 메서드 안에 지정하면 된다.
코드 아래는 Identation 이 사용된 JSON 문자열 표현이다.
'''
jsonString = json.dumps(customer, indent=4)
print(jsonString)

'''
3. JSON 디코딩
JSON 문자열을 Python 타입 (Dictionary, List, Tuple 등) 으로 변경하는 것을 JSON Decoding 이라 부른다.
JSON 디코딩은 json.loads() 메서드를 사용하여 문자열을 Python 타입으로 변경하게 된다.
'''
dict = json.loads(jsonString)
# Dictionary 데이터 확인
print(dict['id'])
print(dict['name'])
for h in dict['history']:
    print(h['date'], h['item'])

'''

'''
import json
#from collections import OrderedDict

# Ready for data
#group_data = OrderedDict()
#albums = OrderedDict()
group_data = {}
albums = {}

group_data["name"] = "여자친구"
group_data["members"] = ["소원", "예린", "은하", "유주", "신비", "엄지"]

albums["EP 1집"] = "Season of Glass"
albums["EP 2집"] = "Flower Bud"
albums["EP 3집"] = "Snowflake"
albums["정규 1집"] = "LOL"
albums["EP 4집"] = "THE AWAKENING"

group_data["albums"] = albums

# Print JSON
print(json.dumps(group_data, ensure_ascii=False, indent="\t"))

# Write JSON to File
fp = open("girlfriend.json", "w", encoding='utf-8')
json.dump(group_data, fp, ensure_ascii=False, indent="\t")
fp.close()

# Read JSON from File
fp = open("girlfriend.json", "r", encoding='utf-8')
read_data = json.load(fp)
fp.close()
print("---------- read json data -----------")
print(read_data)
print(json.dumps(read_data, ensure_ascii=False, indent='\t'))
print("name", read_data['name'])
print('members', read_data['members'])
print("albums", read_data["albums"])
read_data["albums"].update({"EP 5집": "5555"})
print("albums", read_data["albums"])