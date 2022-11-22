def computepay(pay_hours, pay_rate):  # (45,10)
    if pay_hours > 40:
        extra_hours = pay_hours - 40  # 45-40 = 5
        extra_pay = extra_hours * pay_rate * 1.5  # 5 * 10 * 1.5 = 75
        total_pay = (pay_hours - extra_hours) * pay_rate + extra_pay  # 40 * 10 + 75
    else:
        total_pay = pay_hours * pay_rate
    print(total_pay)


computepay(float(input('Enter Hours\n')), float(input('Enter Rate\n')))
