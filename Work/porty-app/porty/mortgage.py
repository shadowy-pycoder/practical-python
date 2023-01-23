# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
std_payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = int(input('Please, enter extra payment start month: '))
extra_payment_end_month = 0
while extra_payment_end_month < extra_payment_start_month:
    extra_payment_end_month = int(input('Please, enter extra payment end month: '))
extra_payment = int(input('Please, enter extra payment: '))


while principal > 0:
    month += 1
    if extra_payment_start_month <= month <= extra_payment_end_month:
        payment = std_payment + extra_payment
    else:
        payment = std_payment
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    if principal < 0:
        principal = 0
    print(f'{month:>4} {total_paid:>10.2f} {principal:.2f}')

print(f'Total paid: {total_paid}')
print(f'Months {month}')
