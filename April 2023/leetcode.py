
"283.Given an integer array , move all 0's to the end of it while maintaining the relative order of the non-zero elements."


l = [0,1,0,3,12]


for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]==0:
            l[i],l[j] = l[j],l[i]


print(l)

"21. MERGE TWO SORTED LISTS"

"You are given  two sorted  lists list1 and list2."

"Merge the two lists in a one sorted list without creating a new list (just by comparing elements in the"
"2 arrays, merge the elements into a single sorted array)"


l1 = [1, 2, 4]
l2 = [1, 3, 4]


for i in range(len(l2)):
    for j in range(len(l1)):
        if l2[i] <= l1[j]:
            l1.insert(j,l2[i])
            print(l1)
            break

"9.palindrome"
n = input("Enter an integer or a string:")

flag = True
for i in range(len(n)//2):
    if n[i].lower() != n[-i-1].lower():
        flag = False
        break

if flag:
    print("palindrome")
else:
    print("Not palindrome")



"COMMON FACTORS"

"Given two positive integers a and b, return the number of common factors of a and b."

"An integer x is a common factor of a and b if x divides both a and b."



class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if a < b:
            l = []
            for i in range(1,a+1):
                if a % i == 0 and b % i == 0:
                    l.append(i)


        else:
            l = []
            for i in range(1, b + 1):
                if a % i == 0 and b % i == 0:
                    l.append(i)

        return len(l)

s = Solution()
print(s.commonFactors(36,63))

"1.Two Sum"

class Solution:
    def twoSum(self, nums, target) :
        l = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    l.append(i)
                    l.append(j)
                    return l


s = Solution()

print(s.twoSum([2,5,5,11],10))