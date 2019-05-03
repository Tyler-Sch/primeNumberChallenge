import pytest
from prime_number_table import prime_number_gen, put_primes_in_table
from first50Primes import first_50_primes

def test_first_50_primes_are_correct():
    x = prime_number_gen()
    fifty_primes = [next(x) for i in range(50)]
    assert fifty_primes == first_50_primes

def test_put_primes_in_table_renders_correctly():
    prime_table_string = put_primes_in_table(3)
    should_be_string = 'x |2 |3 |5 \n2 |4 |6 |10\n3 |6 |9 |15\n5 |10|15|25'
    assert prime_table_string == should_be_string

def test_put_primes_in_table_raises_errors_for_string_input():
    with pytest.raises(Exception) as error_info:
        put_primes_in_table('abc')
    assert error_info.value.args[0] == 'abc is not an integer'


def test_put_primes_in_table_raises_error_for_float_input():
    with pytest.raises(Exception) as error_info:
        put_primes_in_table(3.14)
    assert error_info.value.args[0] == '3.14 is not an integer'

def test_put_primes_in_table_can_take_string_thanks_to_decorator():
    prime_table_string = put_primes_in_table('3')
    should_be_string = 'x |2 |3 |5 \n2 |4 |6 |10\n3 |6 |9 |15\n5 |10|15|25'
    assert prime_table_string == should_be_string

def test_put_primes_raises_error_on_negative_numbers():
    with pytest.raises(Exception) as error_info:
        put_primes_in_table(-19)
    assert error_info.value.args[0] == ('-19 is not greater than 0, please enter'
        + ' a positive number')
