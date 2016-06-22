import unittest
import factorial

class TestFactorial(unittest.TestCase):
	"""Tests for the factorial() function in factorial.py"""

	def test_one_factorial(self):
		self.assertEqual(factorial.factorial(1), 1)

	def test_two_factorial(self):
		self.assertEqual(factorial.factorial(2), 2)

	def test_three_factorial(self):
		self.assertEqual(factorial.factorial(3), 6)

	def test_ten_factorial(self):
		self.assertEqual(factorial.factorial(10), 3628800)

	def test_zero_factorial(self):
		self.assertEqual(factorial.factorial(0), 1)

	def test_for_number_less_than_zero(self):
		self.assertEqual(factorial.factorial(-2), 'invalid input')

	def test_for_string_input(self):
		self.assertEqual(factorial.factorial('two'), 'invalid input')

	def test_for_boolean_input(self):
		self.assertEqual(factorial.factorial(True), 'invalid input')

	def test_for_extremely_large_number(self):
		self.assertEqual(factorial.factorial(4325345), 'input is too large!')

	def test_return_type_of_factorial_calculation(self):
		self.assertIsInstance(factorial.factorial(23), int)