from flask import Flask
from python_exercises import prime
app = Flask(__name__)

@app.route('/<number>')
def primes():
	return prime.primenos(number)

@app.route('/')
def hundred_primes():
	return str(prime.primenos(100))
