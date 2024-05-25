def replace_alphabets(string: str, n: int) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_string = ''
    for letter in string:
        if letter.isalpha():
            index = alphabet.index(letter.lower())
            new_index = (index + n) % 26
            new_string += alphabet[new_index]
        else:
            new_string += letter
    return new_string

string = "The quick brown fox jumps over the lazy dog"
n = 1
print(replace_alphabets(string, n))

def remove_vowels(string):
    vowels = "aeiouAEIOU"
    return "".join([c for c in string if c not in vowels])

string = "Hello, World!"
print(remove_vowels(string))



def is_palindrome(string):
    return string == string[::-1]

string = "racecar"
print(is_palindrome(string))

