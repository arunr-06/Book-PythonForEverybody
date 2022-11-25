# #characters and length of a string
# fruit = 'apple'
# a = len(fruit)
# b = (a-1)
# c = fruit[len(fruit)-1]
# print(a, b, c)
#
# #traverse the characters in string
# fruit = 'apple'
# a = 0
# while a < len(fruit):
#     print(fruit[a])
#     a = a + 1
#
# #traverse the characters in string backwards
# fruit = 'apple'
# a = 1
# while a <= len(fruit):
#     b = fruit[-a]
#     print(fruit[-a])
#     a = a + 1
#
# #Wanted to make change to a string so created a new string
# fruit = 'apple'
# new_fruit = 'new' + fruit
# print(new_fruit)

# # Count number of times letter a is present in the string
#
# def counter(word, letter):
#     n = 0
#     count = 0
#     while int(n) < len(word):
#         if str(letter) == word[n]:
#             count = count + 1
#         n = n + 1
#     print(count)
#
#
# try:
#     counter('appleisanawesomefruit', 'p')
# except:
#     print('Please enter a number')

# #stringinoperator
#
# word = input('Enter the word')
# if word in 'banana':
#     print("There")
# else:
#     print("Not there")

# string comparison

word = input('Enter the word')
if word < 'banana':
    print(word, 'banana')
else:
    print('banana', word)


