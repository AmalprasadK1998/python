"""class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(n//2):
            if 2**i == n:
                return True
            else:
                return False

s = Solution()
s.isPowerOfTwo(16)"""
import math

"""
def isPowerOfTwo(n):
    flag = False
    for i in range(n // 2):
        if 2 ** i == n:
            flag = True
            break
        else:
            continue
    if flag:
        print("Yes")
    else:
        print("No")


n = int(input("enter"))
isPowerOfTwo(n)"""

"""def isPowerOfTwo(n):
    count = 0
    while n % 2 == 0:
        n = n / 2
        count += 1

    if n == 1:
        print(count)
        return True
    else:
        return False


n = int(input("enter"))
isPowerOfTwo(n)"""


"35.Given a sorted array of integers,return the index of the target if target is found , else" \
":return the index where it would have been in the array"

"Try to solve it in log(n) time!"

"""class Solution:
    def searchInsert(self, nums, target):

        flag = False

        for i in range(len(nums)):
            if target - nums[i] == 0:
                flag = True
                break
            elif target - nums[i] < 0:
                flag = True
                break
            else:
                continue
        if flag:
            return i
        else:
            return i+1
s = Solution()

nums = [1,3,5,6]
target = 7

print(s.searchInsert(nums,target))"""


"""class Solution:
    def searchInsert(self, nums, target,count = 0):

        flag = False
        n = len(nums)
        half = len(nums)//2
        mid = len(nums) // 2
        left = nums[:mid]
        count += mid
        right = nums[mid:]


        if n > 1:

            if target < nums[mid]:
                print(left,mid)
                self.searchInsert(left, target,count)

            elif target >= nums[mid]:
                print(right,mid)
                self.searchInsert(right, target,count)

        return count






s = Solution()

nums = [1,3,5,6,7]
target = 5

print(s.searchInsert(nums,target))"""


class Solution:
    def singleNumber(self, nums):
        """for element in nums:
            if nums.count(element) == 1:
                return element"""
        """y = []
        for element in nums:
            if element not in y:
                y.append(element)
            else:
                y.remove(element)
        return y"""



"""s = Solution()
nums = [2,2,4]
print(s.singleNumber(nums))

d = {n:0 for n in nums}
print(d)"""

"""class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for n in nums:
            if nums.count(n)>1:
                return True
        return False"""

"""
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
       numsSet = set(nums)

       return True if len(numsSet) != len(nums) else False


s = Solution()
nums = [1,1,3,3,2]
print(s.containsDuplicate(nums))"""


"""class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[count]= nums[i+1]
                count += 1



        return count,nums
s = Solution()
nums = [1,1,2,3]
print(s.removeDuplicates(nums))"""


"Q.First unique character in a string"

"""s = "amal"
x = []

l = list(s)
for i in l:
    if l.count(i) == 1:
        x.append(i)

print(x[0])

d = {}

for letter in s:
    if letter in d:
        d[letter] += 1
    else:
        d[letter] = 1

print(d)


for key,value in d.items():
    if value == 1:
        break
print(key)"""






"Q.414.Third distinct largest element in the array! "

"solution:1"

"""nums = [-1,3]

nums = set(nums)
nums = list(nums)

if len(nums) >= 3:
    print(sorted(nums)[-3])
else:
    print(sorted(nums)[-1])"""

"solution:2"

"""for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
print(nums)
if len(nums)>= 3:
    print(nums[2])
else:
    print(nums[0])"""



"Q.202.Happy Number"


# 19 is a happy number!
# My solution!
# Runtime : 40 ms...38.3% beats
"""n = 8
x = str(n)
z = int(x)
s = 0
y = [int(x)]
while (1 not in y) and (37 not in y):

    for i in x:
        s += int(i) ** 2
    x = str(s)
    s = 0
    y.append(int(x))

if 1 in y:
        print("Happy",y)
else:
        print("Not Happy",y)"""


# conventional method using set
# runtime:50 ms..8.9% beats

"""class Solution:
    def isHappy(self, n: int) -> bool:

        visit = set()

        while n not in visit:
                visit.add(n)
                n = self.SumofSquares(n)

                if n==1:
                        return True

        return False

    def SumofSquares(self, n: int) -> int:
            output = 0

            while n:
                    digit = n%10
                    digit = digit**2
                    output += digit
                    n = n//10
            return output"""


"Q.485.Max Consecutive ones...Given a binary array nums, return the maximum number of consecutive 1's in the array."
# Method 1 (My method)
"""nums = [1,1,0,1,1,1]

y = []

count = 0
for i in nums:
    if i == 1:
        count += 1

    else:
        count = 0
    y.append(count)


print(max(y),y)"""

# Method 2,less runtime;
"""class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:

        count = 0
        maximum = 0
        for i in nums:
            if i == 1:
                count += 1

            else:
                count = 0

            if count > maximum:
                maximum = count
        return(maximum)"""



"Q.Remove element"

# nums = [3,2,2,3]
# val = 3
#
# for i in range(nums.count(val)):
#     nums.remove(val)
# print(nums)


"Q.15...Three sums....(My solution...test case accepted but time limit exceeded)"
"""nums = [-1,0,1,2,-1,-4]
l = []
y = []
x =[]

for i in range(len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k]==0 :
                y.append(nums[i])
                y.append(nums[j])
                y.append(nums[k])

                if set(y) not in x:
                    x.append(set(y))
                    l.append(y)
                    print(l)
                y =[]

                print(l)"""


# swapping until the middle
# l = [1,2,3,4,5,6]
# print()
# for i in range(math.ceil(len(l)/2)):
#     l[i], l[len(l) - i - 1] = l[len(l) - i - 1], l[i]
#     print(l)
# print()

# swapping until the entire length
# l = [1,2,3,4,5,6]
# for i in range(len(l)):
#     l[i], l[len(l) - i - 1] = l[len(l) - i - 1], l[i]
#     print(l)
# print()


"Don't know about this,n^2 times looping"
# l = [1,2,3,4,5,6]
# count = 0
# for i in range(len(l)):
#     for j in range(len(l)):
#         l[i],l[j] = l[j],l[i]
#         count += 1
#     print(l)








# sammishra sakalam prabadhyee!
# ramarakhava krishnaraghava



"""s = {1,3,5}
m = []
m.append(s)
print(m)"""

"m.add(s)...we cannot do this operation on set ..Type error: unhashable type:'set' "
"But m.append(s) is possible ..I don't know why!"


nums = [1,2,2,3,3,3]

s = set(nums)


max = -1
for i in s:
    if nums.count(i)==i and i > max:
        max = i
print(max)

nums = sorted(nums,reverse=True)
for i in nums:
    if nums.count(i) == i:
        max = i
        break


# 8.string to integer conversion of (an integer in the string)
"""s = "21a2"
size = 0
x = 0
for i in s:
    if 0<= ord(i)-48 < 10:
        size += 1
    elif ord(i)==46:
        break

print(f'size:{size}')
flag = True
count = 0

for i in s:
    # print(ord(i),format(ord(i),'08b'))
    if (s.count('-') + s.count('+')) > 1:
        break

    if i == '+':
        flag = True
    if i == '-':
        flag = False

    elif 0<= ord(i)-48 < 10:
        count += 1
        x += (ord(i) - 48) * (10 ** (size - count))


    elif ord(i)!=32:
        break




if flag and x > (2**31) - 1:
    print((2**31)-1)

elif not flag and x  > 2** 31:
    print(-2**31)

elif flag:
    print(x)

else:
    print(-x)"""



# My solution...52 ms....5.70% beats!

"""digits = [9,9]
for i in range(1,len(digits)+1):
    if digits[-i]!=9:
        digits[-i]+=1
        print(digits)
        break

    elif digits[-i]==9 :
        digits[-i]=0


if sum(digits)==0:
    digits.insert(0,0)
    digits[0]=1

print(digits)"""

# s = "112"

# print(len(s))
# print(s[::-1])



s = ""

d = []
for word in s.split():
    d.append(word)


print(d,len(d))

# Q.389. Find the difference

# Method 1:

s = "taj"
t = "jatt"

for i in t:
    if  s.count(i) != t.count(i):
        print(i)
        break

# Method 2:

x = sum(ord(i) for i in s)
y = sum(ord(j) for j in t)

print(chr(y-x))

class Solution:
    def myPow(self, x: float, n: int,m:float) -> float:
        if n>0:
            m = m * x
            if n == 1:
                print(m)

            self.myPow(x, n - 1,m)

            if n == 1:

                return m


        elif n<0:
            m = m * x
            if n == -1:
                print(1/m)
            self.myPow(x, n + 1, m)



        else:
            return 1


class Solut:
    def myPow(self, x: float, n: int) -> float:
        m = 1
        if n == 0:
            return 1
        elif n > 0:
            while n > 0:
                m = m*x
                n-=1
            return m
        else:
            while n < 0:
                m = m*x
                n+=1
            return 1/m

s = Solut()
print(s.myPow(2,-3))


class Sol:
    def mySqrt(self, x: int) -> int:

        if x > 0:
            y = [i for i in range(1,x) if i**2 <= x]
            return y[-1]


        else:
            return 0


s = Sol()
print(s.mySqrt(10))


l = [1,2]

l = [i**2 for i in range(1,10) if i<10]
print(l)


m = [[1,2,3],[4,5,6],[7,8,9]]

y = []
# [1,2,3,6,9,8,7,4,5]
i,j = 0,0

while j < len(m[0]):

    if m[i][j] not in y:
        y.append(m[i][j])
    j += 1
    if j == len(m[0]):
        j -= 1
        break

while i < len(m):

    if m[i][j] not in y:
        y.append(m[i][j])

    i+=1
    if i == len(m):
        i-=1
        break

while j >= 0:
    if m[i][j] not in y:
        y.append(m[i][j])

    j-=1
    if j < 0:
        j+=1
        break

while i >= 0:
    if m[i][j] not in y:
        y.append(m[i][j])

    i-=1



print(y,f'{i,j}')

salary = [4000,3000,1000,2000]
print(sorted(salary),salary,min(salary))


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        count = 0
        flag = True
        x = abs(dividend)-abs(divisor)

        while x >= 0:
            x = x - abs(divisor)
            count += 1

        if dividend*divisor < 0:
            flag = False
        if flag:
            return count
        else:
            return -count



m = Solution()
print(m.divide(-3,1))


s = "amal"
j = "lama"
print(s==j)

print(s.count('a'))

print(set(s)==set(j))
print(s == j)



d = {s[i]:s.count(s[i]) for i in range(len(s))}

e = {j[i]:j.count(j[i]) for i in range(len(j))}

print(d,e)
print(d==e)

strs = ["eat","tea","tan","ate","nat","bat"]
y = []
m = {}
for i in strs:
    z = []
    d = {i[j]: i.count(i[j]) for j in range(len(i))}
    if d not in m.values():
        m[i] = d
        z.append(i)
        y.append(z)



print(y)
print(m)


# 1002.Finding common characters.

demo = ["bella","label","roller"]
words = ["cool","lock","cook"]

size = len(words)
l = []
for letter in words[0]:
    count = 1
    for word in words[1:size]:
        if letter in word:

            count += 1
            # w = word.replace(letter,' ')
            # words.remove(word)
            # words.append(w)

            print(words)

    if count == size:
        l.append(letter)



print(l,words)
arr = [1,0,2,3,0,4,5,0]



# 1089..Duplicate zeroes

print(f'arr:{arr}')
i=0
while i<len(arr):
    if arr[i]==0:
        arr.pop()
        arr.insert(i,0)
        i+=1

    i+=1


print(f'arr:{arr}')

word = "Humdard"
print([*word])
word = word.replace('d',' ')
print(word)


# 682. Baseball Game
operations = ops = ["5","-2","4","C","D","9","+","+"]
i = 0
y = []
# How to handle nagative integers in the array?
s = '320a'
print(ord('-'))
print(sum(ord(i) for i in s)-97)

while i<len(operations):

    if operations[i] == 'C' and len(y)>0:
        y.pop()
    elif operations[i] == 'D':
        double = 2*y[-1]
        y.append(double)
    elif operations[i] == '+':
        s = y[-1]+y[-2]
        y.append(s)
    else:
        y.append(int(operations[i]))

    print(y)
    i+=1
print(sum(y))






string = "1233"

print(*string)





s = "-34"
print(s.isdigit() or '-' in s)


# 914. X of a Kind in a Deck of Cards

deck = [1,2,3,4,4,3,2,1]
print(min(deck, key=deck.count))

minimum = min(deck, key=deck.count)


m = deck.count(minimum)
print(m)

print('-----------------------------------------------')
# deck =  [1,2,3,4,4,3,2,1]
# deck = [1,1,1,2,2,2,3,3,3]
# deck = [1,2,3,4,5]
# deck = [1]
# deck = [1,1,1,2,2,2,3,3]
deck = [1,1,1,1,2,2,2,2,2,2]
s = set(deck)

l = []

for i in s:
    l.append(deck.count(i))
flag = True
# for i in range(2,min(l)+1):
#     for j in l:
#         if not(j%i == 0 and j%min(l)==0):
#             flag = False
#             print(i,j)
#             break
# if flag:
#     print("True")
# else:
#     print("False")




# l = sorted(l,reverse=True)
#
# print(l)
# print(-sum(l[1:])+l[0])



# No common factors other than 1 for false case but have common factors other than 1 in true case(Given len(l)>1 and len(deck)>1)!


print(f'deck:{deck}')
print(f's:{s}')
print(f'l:{l}')




