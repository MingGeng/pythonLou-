import json
myjson = ''
newjson = ''

with open('data2.json', 'r') as file:
    myjson=json.loads(file.read())
    newjson=json.dumps(myjson,ensure_ascii=False) 
    print(newjson)

with open('data3.json', 'w') as file:
     file.write(json.dumps(newjson, ensure_ascii=False))

