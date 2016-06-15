import unittest
import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
	"""Testing the fizzbuzz
	"""

	def test_returns_fizz_when_divisible_by_three(self):
		"""Test returns fizz when input is divisible by three 
		"""
		self.assertEqual(fizzbuzz.fizz_buzz(3), 'fizz')

	def test_returns_buzz_when_divisible_by_five(self):
		"""Test returns buzz when input is divisible by five 
		"""
		self.assertEqual(fizzbuzz.fizz_buzz(5), 'buzz')

	def test_returns_fizzbuzz_when_divisible_by_fifteen(self):
		"""Test returns fizzbuzz when input is divisible by fifteen 
		"""
		self.assertEqual(fizzbuzz.fizz_buzz(15), 'fizzbuzz')

	def test_returns_true_when_input_is_integer(self):
		"""Test returns True when input is and integer
		"""
		self.assertEqual(fizzbuzz.fi)
