l = [1, 2, 3, 4]
for i in l:
    print(i)

# Since we are able to iterate through the collection l,then l is termed as an "ITERABLE"

# To create an ITERATOR , we use the "iter" keyword
# We can also iterate through an ITERATOR,which means ITERATOR is also ITERABLE
# But, all ITERABLES are not ITERATORS

# create an ITERATOR
l_iterator = iter(l)
print(l_iterator)

# LIST is an ITERABLE but it is not an ITERATOR

# if some object is said to be ITERABLE , it needs to have  a special method called __iter__()
# i.e, if some object has to be looped over , then it needs to have __iter__()
# for loop is ---> calling __iter___() on our object l,i.e,l.__iter() and returning an iterator that can loop over!

print(dir(l))
print(dir(l_iterator))


# An iterator is an object with a state, so that it remembers where it is, during iteration!
# It allows the programmer to traverse through a sequence of data WITHOUT HAVING TO STORE THE ENTIRE DATA IN THE MEMORY

"example : LIST object is not an iterator since we need to store the entire data in the memory and then traverse "
"through it one by one...(every list item is brought into the main memory/RAM) but RANGE object is an iterator since we "
"can traverse through the data one by one without having to store the entire data in the memory"
"...(only needed one is brought into the main memory/RAM)"






"One built-in iterator object in Python is the enumerate iterator. It takes an iterable as input and returns an iterator "
"that generates pairs of elements, one from the input iterable and the other an increasing integer index."

print(next(enumerate(l)))
a,b = next(enumerate(l))
print(a)


# Generators

def squares(limit):
    for i in range(limit):
        yield i**2

# When this function is called, it returns a generator object, which is an iterator that can be used to generate
# the sequence of square numbers up to the limit:
# After the limit , if it is the for loop, it breaks out of the StopIteration Exception
# Else if it is purely using next() on the generator object,it raises StopIteration exception;
square = squares(5)

"""
Using only the next() on iterator , it doesn't handles the StopIteration Exception , thus raises the exception 
after the iteration ends!

print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))"""


print("Using for loop,it handles the StopIteration Exception:")
for num in square:
    print(num)




"An iterator is an object that implements the iterator protocol, which requires it to have two methods: __iter__() and __next__(). "
"The __iter__() method returns the iterator object itself, and the __next__() method returns the next item from the iterator. "
"Iterators are used to iterate over a collection of elements, one at a time, without loading them all into memory at once."

"On the other hand, a generator is a type of iterator that is defined using a function instead of a class."
" Generators are created using a yield statement instead of return. When a generator function is called,"
" it returns a generator object, which can be used to iterate over the sequence of values generated by the function. "
"Like iterators, generators are used to produce a sequence of values one at a time, without loading them all into memory at once."


"The key difference between an iterator and a generator is that a generator is a more convenient and concise way of creating"
" an iterator. With a generator, you don't need to create a separate class with __iter__() and __next__() methods, and you "
"don't need to keep track of the state of the iterator explicitly. Instead, the generator function takes care of all of"
" that for you. Additionally, generators have the added benefit of being able to 'yield' values lazily, which can help "
"reduce memory usage and improve performance for large collections"