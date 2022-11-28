# opening a text file in python

# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     count = count + 1
# print(count)

# # reading the content of a file
#
# fhand = open('mbox-short.txt')
# inp = fhand.read()
# print(len(inp))
# print(inp[:20])

# printing the content of a file

# fhand = open('mbox-short.txt')
# for a in fhand:
#     if a.startswith('From:'):
#         a = a.strip()
#         print(a)

# find a and print the string using find, if and continue functions:

# fhand = open('mbox-short.txt')
# for a in fhand:
#     a = a.strip()
#     if a.find('@uct.ac.za') == -1:
#         continue
#     print(a)

# input file name and retrieve information about the file:

# f = input('Enter the name of the file\n')
# fname = open(f)
# count = 0
# for a in fname:
#     if a.startswith('Subject:'):
#         count = count+1
# print(count)

# Using try and except while opening a file

# f = input('Enter the file name:\n')
# try:
#     fname = open(f)
# except:
#     print('Please recheck the file name')
#     exit()
# count = 0
# for i in fname:
#     if i.startswith('Subject:'):
#         count = count+1
# print(count)

# fname = open('output-short.txt', 'w')
# a = fname.write('What is happening\n')
# print(a)
# b = fname.write('I get it\n')
# print(b)
# fname.close()

# fname = open('output-short.txt', 'w')
# d = fname.write('ddd')
# print(d)

a = '1 2\t 3\n 4'
print(repr(a))




