s = input()
upper, lower, digit, sortl, sortd, sortu, odd, even = "","","","","","","",""
for letter in s:
    if letter.isupper():
        upper = upper + letter
    if letter.islower():
        lower = lower + letter
    if letter.isdigit():
        digit = digit + letter
upper_sorted, lower_sorted, digit_sorted = sorted(upper), sorted(lower), sorted(digit)
for i in upper_sorted:
    sortu = sortu + i
for j in lower_sorted:
    sortl = sortl + j
for k in digit_sorted:
    if int(k)%2 != 0:
        odd = odd + k
    else:
        even = even + k
    sortd = odd + even
final_string = sortl + sortu + sortd
print(final_string.strip())
