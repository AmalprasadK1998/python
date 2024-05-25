# CLOSURES

def main_welcome(msg):
    def sub_welcome():
        print("Welcome to my classroom")
        print(msg)

    return sub_welcome()


main_welcome("hello,how are you?")


# DECORATORS (function within a function / composition of functions)
# passing function as a parameter within another function

def f(x):
    def product(a, b):
        x()
        print(a * b)

    return product(23, 32)


@f  # f applied on y (f(y))
def y():
    print("product:")


# FUNCTION COPY
# Here, the function object is copied to a variable(second reference)
# After that, the first object reference  gets deleted;

def sample_string():
    print("hello")


variable = sample_string
del sample_string

variable()

# LIST COPY(same as function copy)

l = [1, 2, 3, 4]
a = l
del l
print(a)
