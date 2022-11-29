"""""
# Printing the value of a string
a = ['a', 'b', 'c', 12, [13, 14]]
print(a[4])

# Changing the value of a string
a = ['a', 'b', 'c', 12, [13, 14]]
a[0] = 34
print(a)

# Checking if the list contains the element using In operator
a = ['a', 'b', 'c', 12, [13, 14]]
print('a' in a)


# Traversing a list
a = [1, 2, 3, 4, 5]
for i in a:
    print(i)

# Making changes to the elements of the list using index and range
a = [1, 2, 3, 4, 5]
for i in range(len(a)):
    a[i] = a[i] * 2
    print(a[i])
print(range(5))

# Same as the above program except not using index
a = [1, 2, 3, 4, 5]
for i in a:
    i = i * 2
    print(i)

# list operations such as + and *

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

d = a * 3
print(d)

# default funtion:

def routine(c, d=10):
    b = c + 3 + d
    print(b)


routine(10)


# Extending elements of a list and sorting it:

a = [11, 2, 9, 4, 5]
b = [7, 8]
a.extend(b)
print(a)
a.sort()
print(a)

# Deleting elements in list using pop:
a = [1, 5, 33, 345, 2, 5, 32]
c = a.pop(4)
print(a)
print(c)

# Deleting elements in list using remove:
a = [1, 5, 33, 345, 2, 5, 32]
c = a.remove(345)
print(a)
print(c)

# Deleting elements using delete statement:
a = [1, 5, 33, 345, 2, 5, 32]
del a[:4]
print(a)


# Lists and function

a = [1, 5, 6, 2, 8, 11, 3]
b = max(a)
c = min(a)
d = sum(a)
e = len(a)
f = sum(a)/len(a)
print(a, b, c, d, e, f)


# Compute average without list:

total = 0
count = 0
while True:
    n = input('Enter the no:\n')
    if n == 'done':
        break
    else:
        total = total + int(n)
        count = count + 1
average = total / count
print('Total value is:', total, 'Total count is:', count, 'Average is:', average)



# Computer average with a list

nlist = list()
while True:
    n = input('Enter the no:\n')
    if n == 'done':
        break
    else:
        value = float(n)
        nlist.append(value)
print(nlist)
print('sum is:', sum(nlist))
print('length is:', len(nlist))
print('average is:', sum(nlist)/len(nlist))


# Spliting a string into list using delimiters:

a = 'apple.is.good for health'
delimiter = '.'
b = a.split(delimiter)
print(b)

# Joining a list into a string:

a = ['an', 'apple', 'a', 'day']
delimiter = ' '
b = delimiter.join(a)
print(b)

"""""