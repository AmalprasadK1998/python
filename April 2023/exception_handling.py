num_1 = int(input("Enter a number:"))
num_2 = int(input("Enter another number:"))

try:
    print(num_1 / num_2)
except ZeroDivisionError:
    print("division by zero is not defined!")

print("rest of the code !")

# custom exception

"In the given code, the 'as' keyword is used to assign the instance of the error class to a variable named er. "
"This variable can then be used to refer to the instance of the error class and print its message."

"Even though the __str__() method is not defined in the error class, Python will use the default implementation from the base Exception class. "
"The default __str__() method of the Exception class returns the message passed to the constructor of the Exception class when the instance was created."

" In the given code, the error class (which is a child class of the Exception class) overrides the __init__() method of the parent class."

age = int(input("Enter your age:"))


class error(Exception):
    def __init__(self):
        print("You are not ineligible to vote in India!")


try:
    if age >= 18:
        print("You are eligible to vote in India!")

    else:
        raise error

except error as er:
    print(er)

# Another way in which you can use the "Raise" keyword
n = int(input("Enter any positive integer:"))

try:
    if n > 0:
        print("valid")

    else:
        raise ValueError("invalid")

except ValueError as var:
    print(var)


class FiveDivisionError(Exception):
    pass

try:
    num_1 = int(input("Enter a number:"))
    num_2 = int(input("Enter another number:"))

    if num_2 == 5:
        raise FiveDivisionError("cannot divide by five!")
    div = num_1/num_2
    print("quotient:",div)

except (FiveDivisionError,ZeroDivisionError) as v:
    print(v)

print("rest of code!")

"In the given code, the FiveDivisionError class inherits from the built-in Exception class but does not define a constructor."
"Since the Exception class has a constructor that takes a message argument, we can pass a message to the raise statement as a string."


"When the raise statement is executed with the FiveDivisionError class and a message, a new instance of the "
"FiveDivisionError class is created with the message passed as an argument to the constructor of the Exception class."

"what does the constructor of the exception class do with this message argument then?"
"The constructor of the Exception class takes a message argument and assigns it to the 'args' attribute of the exception instance."


"By default, the __str__() method in the Exception class returns the first element of the args tuple, which is typically a string "
"representing the error message."

"If the args tuple contains additional elements, they can be accessed using tuple indexing, for example, e.args[1] to access "
"the second element of the args tuple."

"When defining a custom exception class, we can override the __str__() method to customize the error message format and"
" display any or all elements of the args tuple as needed."


" In your FiveDivisionError class, since you didn't define an __init__() method, it inherits the constructor from the"
" Exception class, which takes a single argument representing the error message."

"When you raise an instance of the FiveDivisionError class with a message like this:"
"raise FiveDivisionError('cannot divide by five!')"


"It creates an instance of FiveDivisionError with the error message 'cannot divide by five!',"
" which is stored in the args attribute as a tuple with a single element."

"So, when you catch the exception and print it using the print(v) statement, it will print the string representation"
" of the exception instance, which by default includes the error message stored in the args attribute."

pin = int(input("Enter the pin:"))
amount = int(input("Enter the amount to withdraw:"))
balance = int(input("Enter your balance:"))

class CannotDebit(Exception):
    pass
try:
    if balance - amount < 1000:
        raise CannotDebit("Sorry you cannot make the transaction!..Rs.1000 is the minimum balance")
except CannotDebit as cd:
    print(cd)

