# creating a tuple

# Create a tuple of integers
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Create a tuple of strings
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# Create a mixed tuple
my_tuple = (1, "apple", True, 3.14)
print(my_tuple)

"=========================================="

# Accessing items in a tuple

# Access the first item in the tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])

# Access the last item in the tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[-1])

# Access a range of items in the tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])

"=========================================="


# Check if an item exists in the tuple
my_tuple = (1, 2, 3, 4, 5)
if 3 in my_tuple:
    print("3 exists in the tuple")
else:
    print("3 does not exist in the tuple")


"=========================================="

# Unpack a tuple
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)
print(b)
print(c)

"=========================================="

# create a tuple of strings and sort them in alphabetical order
my_tuple = ("apple", "banana", "cherry", "date", "fig")
print(sorted(my_tuple))
print(tuple(sorted(my_tuple)))


# sum of integers in a tuple
tuple_1 = (1,2,3,4,5,6,7,8,9,10)
sum = 0

for num in tuple_1:
    sum += num

print(sum)