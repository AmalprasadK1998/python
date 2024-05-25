
# word count and letter count (FREQUENCY)
sentence = "Every action has an equal and opposite reaction"

letter_count = {}
word_count = {}


for letter in sentence:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print(letter_count)


for word in sentence.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


print(word_count)


# Group objects in a list by attributes

class person:

    def __init__(self,name,age):
        self.name = name
        self.age = age


Ram = person("Ram", 24)
Raghav = person("Raghav", 35)
Madhav = person("Madhav", 30)
Jayan = person("Jayan", 30)

people = [Ram, Raghav, Madhav, Jayan]

people_by_age = {}

for individual in people:
    if individual.age not in people_by_age:
        people_by_age[individual.age] = [individual.name]
    else:
        people_by_age[individual.age].append(individual.name)


print(people_by_age)

# Invert dictionary:Swap keys and values in a dictionary to make a new dictionary!
my_dict = {'a':1,'b':2,'c':3,'d':4}
inverted_dict = {}

for key,value in my_dict.items():
    inverted_dict[value] = key

print(inverted_dict)

# FREQUENCY COUNT: Given a list , count the frequency of each element in the list and store the result in a dictionary

l = [0,4,8,1,2,4,8,8,8,9,8]

l_count = {}

for number in l:
    if number not in l_count:
        l_count[number] = 1
    else:
        l_count[number] += 1

print(l_count)


# Finding Anagrams:Given a list of words, group the words into lists of anagrams

words = ["race","care","acre","ear","are","arc"]
anagrams = {}

for word in words:
    sorted_word = "".join(sorted(word))
    if sorted_word not in anagrams:
        anagrams[sorted_word] = [word]
    else:
        anagrams[sorted_word].append(word)

print(anagrams)


# Group by multiple attributes:
# Given a list of objects, group the objects by multiple attributes and store the result in a dictionary

class person:

    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

Ram = person("Ram", 24,"Hyderabad")
Raghav = person("Raghav", 35,"Banglore")
Madhav = person("Madhav", 30,"Kochi")
Jayan = person("Jayan", 30,"Chennai")

people = [Ram,Raghav,Madhav,Jayan]
people_by_age_and_city = {}


for individual in people:
    key = (individual.age,individual.city)
    if key not in people_by_age_and_city:
        people_by_age_and_city[key] = [individual.name]
    else:
        people_by_age_and_city[key].append(individual.name)

print(people_by_age_and_city)


# Find common elements in multiple lists

l1 = [1,2,3,4,5]
l2 = [2,4,6,8]
l3 = [1,2,3,4]

common_elements = {}

for element in l1:
    if element in l2 and element in l3:
        if element in common_elements:
            common_elements[element] += 1
        else:
            common_elements[element] = 1

print(common_elements)

# Group data by category:
# Given a list of items and their category, group the items by category and store the result in a dictionary

items = [{"name":"Apple","category":"fruits"},
         {"name":"Banana","category":"fruits"},
         {"name":"Carrot","category":"vegetable"},
         {"name":"spinach","category":"vegetable"},
         {"name": "beef", "category": "meat"},
         {"name": "chicken", "category": "meat"}
         ]

grouped_items = {}

for item in items:
    key = item["category"]
    value = item["name"]
    if key not in grouped_items:
        grouped_items[key] = [value]
    else:
        grouped_items[key].append(value)

print(grouped_items)


# Mapping data from one form to another
# Given data in one format, map data into another format using a dictionary

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

for key,value in mapping.items():
    result[key] = data[value]

print(result)



