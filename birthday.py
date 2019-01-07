import datetime
currentDate = datetime.date.today()
print(currentDate)
myBday = input('Enter your bday: ')
birthday = datetime.datetime.strptime(myBday, '%m/%d/%Y').date()
print(birthday)
days=birthday-currentDate
print(days.days)