# Python program to test if the given string is palindrome or not (Spaces and punctuations are ignored)
# Digant Kumar

def reverse(string):                            # Returns the reversed string
    return string[::-1]

def is_palindrome(string):
    word = ""
    for s in string:
        if s.isalnum():                         # Checks if the char is alpha-numeric or not
            word = word + s.lower()
            original = word
    temp = reverse(word)
    reversed = temp.lower()
    if original == reversed:                    # If original string is same as the reversed, then palindrome
        return "Is Palindrome"
    else:
        return "Not palindrome"

string = "Doc, note: I dissent. A fast never prevents a fatness. I diet on cod"
print(is_palindrome(string))