maximum = None
while True:
    a = input('Enter a number\n')
    if a == 'done':
        break
    elif maximum is None or int(a) > int(maximum):
        maximum = a
print('Maximum number is', maximum)
