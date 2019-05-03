# Prime Number Multiplication Generator

A command line program that prints out a multiplication table of a given the amount of primes (defaults at 10)

## Requirements
```
python 3.6 or greater
pytest
```

## Installation and Execution:

```
git clone https://github.com/wintermutestoothache/primeNumberChallenge.git
```
with [Virtualenv](https://virtualenv.pypa.io/en/latest/):
```
virtualenv env -p python3.6
source env/bin/activate
pip install -r requirements.txt
```

with out virtualenv:
```
pip install -u pytest
```

To run:

```
cd primeGen
python prime_number_table.py
```
if you like to generate a table other than the default 10 x 10 include an integer
argument for the amount of primes you'd like

ex:
```
python prime_number_table.py 5
```

## To Test:
```
pytest
```


### The Prime Number Generator:
I chose to use a generator based on 'The Sieve of Eratosthenes'.

Generating primes using a brute force method is fine for very low values, but as n increases the amount of operations you need to test for primality increases exponentially.

"The Sieve of Eratosthenes" takes a upper border and constructs an efficient way of generating all primes up to that number by keeping a list of all numbers that are not prime. After the sieve runs, if a number is not in its' list, it is prime. The problem with the sieve in this application is that we need an arbitrary amount of primes, not all primes that exist below a particular border.

To fix this, this implementation takes advantage of pythons generators and dictionaries to produce the arbitrary amount of primes needed and track the sequences of composite integers.

This implementation is computationally and memory efficient, since dictionary look up of potential primes is constant and the only numbers kept in memory are last numbers in the non-prime sequences.
