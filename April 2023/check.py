my_dict = {1:'Akhil',
           2:'Akshay',
           3:'Nair',
           4:'Jaadu'}

l = [1,3,5,7,9,11,13,15,17,19]

# dictionary comprehension
inverted_my_dict = {value:key for key,value in my_dict.items()}

print(inverted_my_dict)

# list comprehension
l_square = [n**2 for n in l]

print(l_square)

items = [{"name":"Apple","category":"fruits"},
         {"name":"Banana","category":"fruits"},
         {"name":"Carrot","category":"vegetable"},
         {"name":"spinach","category":"vegetable"},
         {"name": "beef", "category": "meat"},
         {"name": "chicken", "category": "meat"}
         ]

items_by_category = {}

for item in items:
    key = item['category']
    value = item['name']
    if key not in items_by_category:
        items_by_category[key] = [value]
    else:
        items_by_category[key].append(value)

print(items_by_category)

items_by_category = {item['category']: [i['name'] for i in items if i['category'] == item['category']] for item in items}


print(items_by_category)

data = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "gender": "male"
}

mapping = {
    "fname": "first_name",
    "lname": "last_name",
    "gender": "gender"
}

result = {}

for key in mapping:
    for value in data.values():
        result[key] = value

print(result)

result = {key:value for key in mapping for value in data.values()}

print(result)