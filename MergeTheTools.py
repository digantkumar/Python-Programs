import sys
from collections import OrderedDict
def merge_tools(string,k):
    new_str = ""
    if len(string)%k == 0:
        for i in range(len(string)):
            if i%k != 0:
                new_str = new_str + string[i]
            else:
                new_str = new_str + "\n"
                new_str = new_str + string[i]
    else:
        sys.exit("Enter a factor only")
    str_split = new_str.split()
    new_str1 = ""
    listi = []
    for i in str_split:
       a = ''.join(OrderedDict.fromkeys(i).keys())
       listi.append(a)
    for j in listi:
        new_str1 = new_str1 + j + "\n"
    print(new_str1.strip())

string, k = input(), int(input())
merge_tools(string, k)