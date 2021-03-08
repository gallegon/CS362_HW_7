import unittest
import fizzbuzz #the file that contains the program will be named this

class TestFizzbuzz(unittest.TestCase):
	def test_fizzbuzz_3(self):
		self.assertEqual(fizzbuzz.fizzbuzz(3), "Fizz")
	def test_fizbuzz_5(self):
		self.assertEqual(fizzbuzz.fizzbuzz(5), "Buzz")
	def test_fizbuzz_15(self):
		self.assertEqual(fizzbuzz.fizzbuzz(15), "FizzBuzz")

	# more ambitious test to test ALL cases.  Not sure if it'll work when I
	# get around to writing the function
	def test_fizzbuzz_100(self):
		for i in range(1,101):
			actualValue = fizzbuzz.fizzbuzz(i)
			if i % 3 == 0 or i % 5 == 0:
				if i % 3 == 0 and i % 5 == 0:
					expectedValue = "FizzBuzz"
				elif i % 3 == 0:
					expectedValue = "Fizz"
				else:
					expectedValue = "Buzz"
			else:
				expectedValue = i

			self.assertEqual(actualValue, expectedValue)

#	def test_fizzbuzz_rand(self):
