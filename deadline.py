import datetime
currentDate = datetime.date.today()
print(currentDate)
input = input('Enter the deadline of your project: ')
deadline = datetime.datetime.strptime(input, '%m/%d/%Y').date()
print(deadline)
days=deadline-currentDate
weeks=0
daysLeft= days.days
while daysLeft >= 7:
    daysLeft=daysLeft-7
    weeks+=1
if weeks == 0:
    print('You have ' + str(daysLeft)+" days to your deadline")
else:
   print('You have '+str(weeks)+ " weeks and " + str(daysLeft)+" days to your deadline")

#elif for else if