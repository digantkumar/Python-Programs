# Digant Kumar
# Python program that outputs the twenty most occurring words in a text.

def analyize(file):
    textfile = open(file,"r")
    content = textfile.read()           # Reading the contents of a textfile
    word_split = content.split()
    word_dict = {}
    count = 0
    for word in word_split:
        if word.isalnum():
            word = word.lower()         # Converting words to lowercase, and only accepting alphanumeric characters
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    sorted_dict = sorted(word_dict.items(), key=lambda x:x[1], reverse=True)    # Sorting the dictionary in decreasing order.
    for key,value in sorted_dict:
        if count < 20:                   # For top 20 words
            count += 1
            print(key)
        else:
            break
    return ""

file = "SherlockHolmes.txt"
print(analyize(file))