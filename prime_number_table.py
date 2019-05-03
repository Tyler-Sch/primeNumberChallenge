import sys
from itertools import count

def prime_number_gen():
    """
        a prime number generator based on sieve of Eratosthenes
        to use:
            x = prime_number_gen()
            then call next(x) to generate as many primes as you like
    """
    not_prime_dict = {}
    yield 2

    for number in count(3, 2):
        if not not_prime_dict.get(number):
            yield number
            not_prime_dict[number ** 2] = number
        else:
            prime_factor = not_prime_dict.pop(number)
            next_num_in_sequence = number + (2 * prime_factor)
            while not_prime_dict.get(next_num_in_sequence):
                next_num_in_sequence += 2 * prime_factor

            not_prime_dict[next_num_in_sequence] = prime_factor


def inputValidation(func):
    """
        decorator to insure input is of the correct format
        checks for:
            - floats
            - strings that dont convert to integers
            - negative numbers
    """
    def wrapper(n):
        if type(n) == float:
            raise TypeError(f'{n} is not an integer')
        try:
            n = int(n)
        except ValueError:
            raise TypeError(f'{n} is not an integer')
        if n < 1:
            raise ValueError(f'{n} is not greater than 0, ' +
                'please enter a positive number'
            )
        return func(n)

    return wrapper


@inputValidation
def put_primes_in_table(n):
    """
        input:
            an integer greater than 0
        output:
            a prime number multiplication table in a printable string format
    """
    # generate primes
    prime_gen = prime_number_gen()
    primes = [next(prime_gen) for _ in range(n)]
    # add a 1 to the beginning so table includes the primes themselves
    primes_with_one = [1] + primes
    # compute mutiplication table
    prime_table = [
        [top_num * left_num for top_num in primes_with_one]
        for left_num in primes_with_one
    ]
    # set column width to value of digits in the largest number
    col_width = len(str(primes[-1] ** 2))
    # make lists into strings with a border character inbetween
    prime_string_grid = []
    for row in prime_table:
        table_row = (
            "|".join(
                [str(num).ljust(col_width) if num != 1 else 'x'.ljust(col_width)
                    for num in row]
            )
        )
        prime_string_grid.append(table_row)
    # return grid as one string with new line separators
    return '\n'.join(prime_string_grid)



if __name__ == '__main__':
    try:
        n = sys.argv[1]
    except IndexError:
        n = 10


    print(put_primes_in_table(n))
