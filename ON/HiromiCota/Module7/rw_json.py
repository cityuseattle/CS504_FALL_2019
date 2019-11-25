import json



# 4 lines, 'cause reasons
json_data = open('example.json')
# go get some values
py_value = json.loads(json_data.read())

for i in range(len(py_value)):
    # print dictionary type of the data
    print(py_value[i])
    #adding try/except block because this code WILL throw an error with this dataset
    try:
        print("Email:", py_value[i]['email'])
    except KeyError:
        print("No email.")
    print()


# write JSON
python_dict = {
    'name': 'Bob',
    'age' : 44,
    'isEmployed': True,
    'balance': None
}, {
    'name': 'Alice',
    'age': 40,
    'isEmployed': False,
    'balance': 0
}

write_file = open('example2.json', 'w')
json.dump(python_dict, write_file, indent=4)
write_file.close()