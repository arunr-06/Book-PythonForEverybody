eng2sp = dict
eng2sp = {'one': 'two', 'two': 'dos'}
print(eng2sp)
print(len(eng2sp))
print('one' in eng2sp)

a2b = list(eng2sp.values())
print(a2b)


# Counting the number of times a letter in found in a word

word = 'leapplepies'
d = dict()
for i in word:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1
print(d)

# returning the values of the key

diction = {'a': 1, 'b': 2}
print(diction['c'])
print(diction.get('a', 0))
print(diction.get('c', 0))


# Counting the number of times letters exist in a word

word = 'leapplepies'
d = dict()
for i in word:
    d[i] = d.get(i, 0) + 1
print(d)

# Counting the words in a file using the get function in dictionary 

fhand = open('words.txt')
a = fhand.read()
b = a.split()
c = dict()
for i in b:
    c[i] = c.get(i, 0) + 1
print(c)


# Traversing the dictionary using the for loop and printing the corresponding keys

ant = {'a': 'g', 'b': 4, 'c': 5, 'd': 6}
for i in ant:
    print(i, ant.get(i, 0))
    print(i, ant[i])


# Using for loop and condition in dictionary:

ant = {'a': 3, 'b': 4, 'c': 5, 'd': 6}
for i in ant:
    if ant[i] > 5:
        print(i, ant.get(i, 0))


ant = {'b': 3, 'e': 4, 'x': 5, 'g': 6}
new_list = list()
new_list = ant.keys()
print(new_list)
a = new_list.sort
print(a)
