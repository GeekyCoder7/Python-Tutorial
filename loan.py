loan = int(input('Enter the cost of your loan\n'))
interest = int(input('Enter the interest rate of the loan\n'))
years = int(input('Enter the number of years of the loan\n'))
numberOfPayments=years*12
interest = float(interest)/100/12
monthlyPayments = loan * (interest * (1 + interest) ** numberOfPayments) / ((1 + interest) ** numberOfPayments - 1)

print('Your monthly payment is ' + str(monthlyPayments))