import json

a =[{'秦海峰':53},{'张航':63},{'刘晰月':55}]
print(a,type(a))
json1 = json.dumps(a,ensure_ascii=False)
print(json1,type(json1))
list1 = json.loads(json1)
print(list1,type(list1))
