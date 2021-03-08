def isLeapyear(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False

print("Enter a year to check: ")

yearToCheck = int(input())

if isLeapyear(yearToCheck) == True:
	print(str(yearToCheck) + "is a leap year")
else:
	print(str(yearToCheck) + "is NOT a leap year")
