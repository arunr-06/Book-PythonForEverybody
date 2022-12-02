"""""
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
        d.append(e)
        #print(d)
        count = count + 1
d.sort()
print(d)
print(count)


# Parsing the line
fhand = open('mbox-short.txt')
for line in fhand:
    line1 = line.rstrip()
    if line1.startswith('From '):
        line2 = line1.split()
        print(line2[1])
    else:
        continue

"""""

#maximum and minimum number in a list:

list1 = list()
while True:
    line = input('Enter the number\n')
    if line == 'done':
        break
    elif not list1:
        list1.append(line)
    else:
        list1.append(line)
print(list1, max(list1), min(list1))

