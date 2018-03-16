def rot_13(message):
    #ceaser code, ROT 13, decoding the message
    dict = {}
    result = ""
    uppercase = range(65, 91)
    lowercase = range(97, 123)
    for c in uppercase:
        if c < 78:
            dict[chr(c)] = chr(c + 13)
        else:
            dict[chr(c)] = chr(c - 13)
    for c in lowercase:
        if c < 110:
            dict[chr(c)] = chr(c + 13)
        else:
            dict[chr(c)] = chr(c - 13)

    dict[" "] = " "
    dict["!"] = "!"

    for i in message:
        result += dict[i]
    return result


print(rot_13('V NZ YRNEAVAT CLGUBA JVGA FUR PBQRF NPNQRZL!'))


