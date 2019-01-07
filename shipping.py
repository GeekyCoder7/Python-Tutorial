amount = int(input('Enter the amount for your total purchases in usd$: '))
if amount < 50:
    amount += 10
    freeShipping=False
else:
    print('Shipping is free')
    freeShipping=True
if freeShipping:
    print('Final total: '+str(amount)+"$ \n")
else:
    print('Final total: '+str(amount)+"$ (including 10$ shipping cost) \n")

