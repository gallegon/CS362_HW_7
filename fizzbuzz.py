def fizzbuzz(i):
	if i % 3 == 0 or i % 5 == 0:
		if i % 3 == 0 and i % 5 == 0:
			return "FizzBuzz"
		elif i % 3 == 0:
			return "Fizz"
		else:
			return "Buzz"
	else:
		return i

for i in range(1,101):
	print(str(fizzbuzz(i)))
