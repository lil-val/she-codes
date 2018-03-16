movie = ['The Notebook', 'Maleficent', 'Batman v Superman', 'Black Swan', 'Gone Girl', 'War of the Worlds', 'Just Married']
actor = ['Rachel McAdams', 'Angelina Jolie', 'Gal Gadot', 'Natalie Portman', 'Rosamund Pike', 'Dakota Fanning', 'Brittany Murphy']
#Ex 9.1
my_List = [m + ' is played by ' + a for (m, a) in zip(movie, actor)]
print(my_List)

#Ex9.2
movies = {k: v for (k, v) in zip(movie, actor)}
print(movies)

#Ex9.3
my_movies = {k + ' is played by ' + v for (k, v) in movies.items()}
print(my_movies)

#Ex9.4
num_list = [n * 100 for n in range(1, 10) if n % 2 == 0]
print(num_list)

#Ex9.5
num_list1 = [n * 100 if n % 2 == 0 else n for n in range(1, 10)]
print(num_list1)

#Ex9.6
seven_boom = ['Boom' if n % 7 == 0 else n for n in range (1, 100)]
print(seven_boom)

#Ex9.7
sum = lambda x, y: x + y
print(sum(3, 4))
print(sum(7, 100))

#Ex9.8
joules = [5000, 8000, 10000, 6000, 12000]
j_cal = [(j, cal) for (j, cal) in zip (joules, map(lambda x: x / 4184, joules))]
print(j_cal)

#Ex9.9
print([(x, y) for x in range(1, 7) for y in range(1, 7)])

#Ex9.10
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(list(filter(lambda x: x == "Python", languages)))
