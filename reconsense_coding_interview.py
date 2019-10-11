input = [{'name': 'John', 'value':10},
         {'name': 'Bob','value': 20},
         {'name': 'John','value': 30},
        {'name': 'Doe','value': 40}]

#  expected output:
# Name = ['John', 'Bob', 'Doe']
# Value = [40, 20 , 40]

name = []
value = []
for i in input:
    if i['name'] in name:
        index = name.index(i['name'])
        value[index] = value[index] + i['value']
    else:
        name.append(i['name'])
        value.append(i['value'])
        
print("Name = ", name)
print("Value = ", value)