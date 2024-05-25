# 1. Factorial
n = int(input("enter any non negative integer:"))


def fact(n):
    if n >= 1:
        return n * fact(n - 1)
    else:
        return 1


f = fact(n)
print(f)

print("------------------------")

# 2. palindrome

s = input("Enter any string:")
n = len(s)

flag = True
for i in range(n // 2):
    if s[i].lower() != s[-i - 1].lower():
        flag = False
        break

if flag:
    print("The given string is a palindrome!")
else:
    print("The given string is not palindrome!")

print("------------------------")

# 3. Fibonacci Sequence
n = int(input("How many terms:"))


def f(n):
    if n > 1:
        return f(n - 1) + f(n - 2)
    else:
        return n


print("------------------------")

# 4. check if the number of terms is valid !

if n > 0:
    sum = 0
    for i in range(n):
        print(f(i))
        sum = sum + f(i)

    print(f"sum upto {n} terms:{sum}")

else:
    print("please enter a positive integer!")

print("------------------------")

# 5.prime numbers between x and y

x = int(input("Enter any positive integer:"))
y = int(input("Enter another positive integer:"))

print(f"prime numbers between {x} and {y} are:")
for i in range(x + 1, y):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break

    if flag:
        print(i)

print("------------------------")

# 6. GCD of m and n

m = int(input("Enter any positive integer:"))
n = int(input("Enter another positive integer:"))

def gcd(m, n):
    cf = 1
    if m < n:
        for i in range(2, m + 1):
            if m % i == 0 and n % i == 0:
                cf = i

    else:
        for i in range(2, n + 1):
            if m % i == 0 and n % i == 0:
                cf = i

    return cf
print(f"Greatest common divisor of {m} and {n} is {gcd(m, n)}")



print("------------------------")




# 7.Finding duplicates within a list

l = []
unique = []
n = int(input("Enter the size of the list:"))

for i in range(n):
    entry = int(input(f"Enter element {i}:"))
    l.append(entry)

print(l)

print("The duplicates in the lists are:")

for item in l:
    if item not in unique:
        unique.append(item)
    elif item in unique and l.count(item)==2:
        print(item)

print(f"list without any duplicates:{unique}")


print("------------------------")

