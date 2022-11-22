# 40 * 10 = 400, 5 * 15 = 75
try:
    hours = int(input('Enter Hours\n'))
    rate = int(input('Enter Rate\n'))
    extra_hours = hours - 40
    extra_rate = rate * 1.5
    extra_pay = extra_hours * extra_rate
    if hours > 40:
        pay = 40 * rate + extra_pay
    else:
        pay = hours * rate
    print('Pay:', pay)
except:
    print('Error, please enter a numeric digit')
