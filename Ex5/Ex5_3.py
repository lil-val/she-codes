def char_freq(string):
    #the function get a strin and returns a dictionary
    #that counting the frequency og each character in the string
    freq = {}
    for i in string:
        value = string.count(i)
        freq[i] = value
    return freq


print(char_freq("abzz"))
print(char_freq("lilach vald-levi"))
print(char_freq('bla bla bla'))
