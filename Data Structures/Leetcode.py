def roman_to_int(s: str) -> int:
    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    integer = 0
    for i in range(len(s)):
        if i > 0 and roman_dict[s[i]] > roman_dict[s[i-1]]:
            integer += roman_dict[s[i]] - 2 * roman_dict[s[i-1]]
        else:
            integer += roman_dict[s[i]]
    return integer

print(roman_to_int("XXI")) # Output: 21
print(roman_to_int("MCMXCIV")) # Output: 1994


def lengthOfLastWord(s: str) -> int:
    s = s.strip()  # remove leading and trailing spaces
    if not s:
        return 0
    return len(s.split()[-1])


s = "Hello World"
print(lengthOfLastWord(s))  # Output: 5


class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
        return rev if -2**31 <= rev <= 2**31-1 else 0

s=Solution()
print(s.reverse(32))
