total = 0
count = 0
while True:
    a = input("Enter\n")
    try:
        if a == 'done':
            break
        else:
            total = total + int(a)
            count = count + 1
    except:
        print('bad data')
print(total, count, total / count)
