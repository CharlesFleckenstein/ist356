grade = float(input('Enter grade:'))
letter = ''
if grade >120 or grade <0:
    letter = 'invalid'
elif grade >= 95:
    letter = 'A'
elif grade >=75 and grade < 95:
    letter = 'B'
elif grade >=50 and grade < 75:
    letter = 'C'
elif grade <50:
    letter = 'F'
print(letter)