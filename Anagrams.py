# Program to check if two words are anagrams of each other i.e same number of each letter occurring in the words
# Digant kumar

def is_anagram(word1, word2):
    dict1 = {}        # Defining two dictionaries for the two words
    dict2 = {}
    for w1 in word1:
        if w1.isalpha():              # Only checking for alphabetical words
            w1 = w1.lower()           # Converting to lower case
            if w1 in dict1:            # Storing the word in the dictionary
                dict1[w1] += 1
            else:
                dict1[w1] = 1
    for w2 in word2:
        if w2.isalpha():
            w2 = w2.lower()
            if w2 in dict2:
                dict2[w2] += 1
            else:
                dict2[w2] = 1
    if dict1 == dict2:                   # If the two dictionaries match then the words are anagrams, else not
        return "The given words are anagrams of each other"
    else:
        return "Not anagrams"

word1 = "listen"
word2 = "SiLENT"
print(is_anagram(word1,word2))