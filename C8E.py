# find the number of unique words in a file

shakes = open('romeo.txt')
lista = list()
count = 0
for i in shakes:
    a = i.split()
    for j in a:
        b = j.split()
        print(b)
        if b in lista:
            print('There already')
            continue
        else:
            print('Not there')
            lista.append(b)
            count = count + 1
print(count)
print(lista)

# Find the number of unique words in a sentence

a = 'arun is doing well arun will do well arun has always done well'
b = a.split()
d = list()
count = 0
for i in range(len(b)):
    #print(b[i])
    e = b[i]
    if e in d:
        #print('there already')
        continue
    else:
        #print('not there')
        d.append(b[i])
        #print(d)
        count = count + 1
d.sort()
print(d)
print(count)

