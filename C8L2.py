"""""
# printing a part of a line(day) that begin with a certain keyword(from)

fhand = open('mbox-short.txt')
for i in fhand:
    i = i.rstrip()
    b = i.split()
    if i.startswith('From') and len(b) > 2:
        print(b[2])

# Find if the list has same object:

a = [1, 2, 3]
b = [1, 2, 3]
c = b
print(b is c)
print(a is b)


# Changing the value of the reference:

b = [1, 2, 3]
c = b
c[2] = 66
print(b)

# Passing list as arguments inside a function

def del_head(t):
    del t[0]


a = [1, 4, 6, 44]
del_head(a)
print(a)

"""""
