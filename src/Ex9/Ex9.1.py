def anagram(s, t):
    if len(s) != len(t):
        return False
    if sorted(s) == sorted(t):
        return True
    return False


print(anagram('dog', 'odg'))
print(anagram('abcd', 'bdhr'))
print(anagram('abcd', 'abc'))

