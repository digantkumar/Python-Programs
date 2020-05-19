# Program to count the number of words, letters and lines in a textfile
# Digant Kumar

textfile = "textfile.txt" #Enter file name here
file = open(textfile,"r")

#Initializing all the counters required
num_lines = 0
num_letters = 0
num_words = 0

# Defining the punctuation as we don't require them.
punctuations = ":,;!?!()-."
for line in file:
    num_lines += 1
    word_split = line.split()
    for word in word_split:
        if word == " ":
            continue
        num_words += 1
    for letter in line:
        if letter ==" ":
            continue
        if letter not in punctuations:
            num_letters += 1
print("Total number of lines in the file:",num_lines)
print("Total number of letters in the file:",num_letters)
print("Total number of words in the file:",num_words)