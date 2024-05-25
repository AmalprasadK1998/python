# custom for loop

def my_for_loop(iterable):
    iterator = iter(iterable)

    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break


l = [1, 2, 3, 4, 5]
my_for_loop(l)


# generators to create a custom range object which is an iterator
# Normally, the built-in range object is not an iterator by itself;


def Custom_Range(m, n):
    for i in range(m, n):
        yield i


# The generator function returns a generator object when it is called!
# Here,it doesnot execute the call unlike normal functions
# Rather, it executes the code one at a time using next();
# for convenience, we may use a for loop which automatically calls the next()
# and handles the StopIteration exception;

a = Custom_Range(1, 4)

print("custom range:")

while True:
    try:
        print(next(a))  # Output: 1
        print(next(a))  # Output: 2
        print(next(a))  # Output: 3
        print(next(a))  # Raises StopIteration implicitly
    except StopIteration:
        print("Range is exhausted!")
        break

print()
print("Using my 'CUSTOM FOR LOOP' on 'CUSTOM RANGE' without any message:")
my_for_loop(Custom_Range(1, 10))
