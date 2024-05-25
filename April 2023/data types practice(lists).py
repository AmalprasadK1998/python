# Remove duplicates from a list

my_list = [1, 2, 3, 3, 4, 4, 5, 5]

l = []

for i in my_list:
    if i not in l:
        l.append(i)
print(l)

# using predefined functions

new_list = list(set(my_list))
print(new_list) # Output: [1, 2, 3, 4, 5]


# add elements into a list(append),"on top"

"""l = []
n = int(input("Enter the size of the list:"))

for i in range(n):
    num = int(input(f"Enter the element {i+1}:"))
    l[i:i] = num

print(l)"""


my_list = []
my_list_length = 5

for i in range(my_list_length):
    element = input(f"Enter element {i+1}: ")
    my_list[i:i] = [element]

print("Final list:", my_list)





