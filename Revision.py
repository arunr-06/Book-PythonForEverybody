largest = None
numbers = [57, 20, 995, 33, 8]
print(max(numbers))

for n in numbers:
    if largest is None or n > largest:
        largest = n
    print('loop:', n, largest)
print('largest:', largest)
