def find_repeats(fname):
    textfile = open(fname,"r")
    content = textfile.read().lower()
    new_word = ""
    for word in content:
        if word == "." or word == "?" or word == ",":
            continue
        else:
            new_word = new_word + word
    word_split = new_word.split()
    for word in range(len(word_split)-1):
        if word_split[word] == word_split[word + 1]:
            print("Repeated word found: ", word_split[word])
    return ""
