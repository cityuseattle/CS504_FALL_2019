import json

json_data=open('example.json')

py_value=json.loads(json_data.read())

for i in range(len(py_value)):
    print(py_value[i])
    print("Email:",py_value[i]['email'])
    print()

python_dict={
    'name':'Bob',
    'age':44,
    'isEmployed':True,
    'balance':None
},{
    'name':'Alice',
    'age':40,
    'isEmployed':False,
    'balance':0
}
write_file=open('example2.json','w')
json.dump(python_dict,write_file,indent=4)
