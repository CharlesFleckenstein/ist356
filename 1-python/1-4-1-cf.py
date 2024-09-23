from datetime import datetime,timedelta
#only importing hte specific things typically in code datetime.(function) woudl be used

today = datetime.now()
print(today)


birthday = input("Enter your birthday: ")
test = datetime.strptime(birthday, "%m/%d/%Y")
test = test + timedelta(days=1)
test_str = test.strftime('%A, %B %d, %Y')
print(test_str)
