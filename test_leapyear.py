import unittest
import leapyear # will be the name of the file that contains leapyear functions

class TestLeapyear(unittest.TestCase):
	def test_leapyear_0003(self):
		self.assertEqual(leapyear.isLeapyear(3), False)
	def test_leapyear_900(self):
		self.assertEqual(leapyear.isLeapyear(900), False)
	def test_leapyear_1600(self):
		self.assertEqual(leapyear.isLeapyear(1600), True)
	def test_leapyear_3412(self):
		self.assertEqual(leapyear.isLeapyear(3412), True)

if __name__ == '__main__':
	unittest.main()
