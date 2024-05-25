# Create a dictionary
my_dict = {
    "apple": 3,
    "banana": 2,
    "orange": 4,
    "pear": 1
}

# Accessing values in the dictionary
print(my_dict["apple"])  # Output: 3

# Updating values in the dictionary
my_dict["banana"] = 5
print(my_dict)  # Output: {'apple': 3, 'banana': 5, 'orange': 4, 'pear': 1}

# Adding a new key-value pair to the dictionary
my_dict["grape"] = 2
print(my_dict)  # Output: {'apple': 3, 'banana': 5, 'orange': 4, 'pear': 1, 'grape': 2}

# Removing a key-value pair from the dictionary
del my_dict["pear"]
print(my_dict)  # Output: {'apple': 3, 'banana': 5, 'orange': 4, 'grape': 2}

# Checking if a key exists in the dictionary
if "banana" in my_dict:
    print("Yes, 'banana' is one of the keys in the dictionary.")

# Looping through the keys in the dictionary
for key in my_dict:
    print(key)  # Output: apple, banana, orange, grape

# Looping through the values in the dictionary
for value in my_dict.values():
    print(value)  # Output: 3, 5, 4, 2

# Looping through both keys and values in the dictionary
for key, value in my_dict.items():
    print(key, value)  # Output: apple 3, banana 5, orange 4, grape 2



# Nested dictionary!

car1_model= {'1960': 'Mercedes'}
car2_model = {'1998': 'Qualis'}
car3_model = {'2000': 'Alto'}
car4_model = {'2005': 'Lancer'}


car_type = {'car1': car1_model,
            'car2': car2_model,
            'car3': car3_model,
            'car4': car4_model}

print(car_type)

# retrieving elements in a dictionary using indexing !
print(car_type['car2']['1998'])


# key 1
for key in car_type:
    print(key)

# key 2
for value in car_type.values():
    for key in value:
        print(key)

# value 1
for value in car_type.values():
    print(value)

# value 2
for value in car_type.values():
    for value in value.values():
        print(value)


# key , value (pair 1)
for key,value in car_type.items():
    print(key,value)

# key , value (pair 2)
for key, value in car_type.items():
    for key,value in value.items():
        print(key,value)