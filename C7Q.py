# input a file name and print the content of the file in upper

# file_name = input('Enter a file name')
# file = open(file_name)
# for line in file:
#     b = line.strip().upper()
#     print(b)

#  find the average float value given the line begins with a particular string

user_input = input('Enter the file name\n')
try:
    file = open(user_input, 'r')
    count = 0
    summation = 0
    for line in file:
        if line.startswith('X-DSPAM-Confidence:'):
            a = line[20:]
            b = a.strip()
            count = count + 1
            summation = summation + float(a)
    d = summation / count
    print(d)
except:
    print('Please recheck the file name')


