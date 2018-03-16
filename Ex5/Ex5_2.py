def same_first_last(strings):
    #sum the number of strings that len >= 2 and first and last letters are equal
    result = 0
    for i in strings:
        if len(i) >= 2 and i[0] == i[-1]:
            result += 1
    return result


print(same_first_last(['aba', 'xyz', 'aa', 'x', 'bbb']))
print(same_first_last(['x', 'xy', 'xyx', 'xx', ""]))
