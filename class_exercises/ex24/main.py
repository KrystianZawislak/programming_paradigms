from math import isqrt
from time import perf_counter

def count_time(function):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = function(*args, **kwargs)
        end = perf_counter()
        print(end - start)
        return result
    return wrapper

def create_the_sieve(interval_end, interval_start = 2):
    sieve = []
    for number in range(interval_start, interval_end+1):
        sieve.append(number)
    return sieve

def clear_the_sieve(sieve):
    cleared_sieve = []
    for record in sieve:
        if record is not False:
            cleared_sieve.append(record)
    return cleared_sieve
    
@count_time    
def sieve_eratosthenes(interval_end, interval_start = 2):
    sieve = create_the_sieve(interval_end)
    strainer = 2
    while strainer**2 <= interval_end:
        for i in range(strainer**2 - interval_start, len(sieve), strainer):
            sieve[i] = False
        strainer += 1
    return clear_the_sieve(sieve)
    
@count_time
def division_method(interval_end, interval_start = 2):
    prime_numbers = [2]
    
    for candidate_number in range(3, interval_end + 1, 2):
        for trial_divisor in range(3, isqrt(candidate_number) + 1, 2):
            if candidate_number % trial_divisor == 0:
                break
        else:
            prime_numbers.append(candidate_number)
    
    return prime_numbers
    
def main():
    sieve = sieve_eratosthenes(100000)
    divisions_primes = division_method(100000)
    
if __name__ == "__main__":
    main()
