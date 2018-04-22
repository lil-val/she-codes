# create txt file containing 15 lines, each with 1 word
my_file = open('myFile.txt', 'w')
my_file.write('dog\n')
my_file.write('cat\n')
my_file.write('lion\n')
my_file.write('elephant\n')
my_file.write('snake\n')
my_file.write('bear\n')
my_file.write('penguin\n')
my_file.write('snail\n')
my_file.write('tiger\n')
my_file.write('wolf\n')
my_file.write('chicken\n')
my_file.write('sheep\n')
my_file.write('cow\n')
my_file.write('horse\n')
my_file.write('bee\n\n')
my_file.close()

reverse_file = open('reverse.txt', 'w')
with open('myFile.txt', 'r') as reading_file:
    for line in reading_file:
        reverse_file.write(line[::-1])
reverse_file.close()

with open('reverse.txt', 'a') as combined_file:
    with open('myFile.txt', 'r') as reading_file:
        for word in reading_file:
            combined_file.write(word)
