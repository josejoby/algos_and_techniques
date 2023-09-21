from perf_measurer import log_time

# to find all primes less than or equal to a given number
# this is an optimised version of sieve_of_eratosthenes

@log_time
def sieve_of_eratosthenes(N):
    """
    1. Assume all numbers from 2 to N are prime
    2. Start from 2 and mark all multiples of 2 as not-prime
    3. After #2, count of numbers that are still marked as prime 
    """
    rbound = N+1
    isPrime = [True]*rbound # idx is a prime if isPrime[idx] == True
    isPrime[0] = isPrime[1] = False # 0 and 1 are not a prime
    i=2
    while i*i <= N: # iterate through all numbers from 2 to sqrt(N)
        if isPrime[i]: # if the number is prime, mark all of its mulitples as not-prime
            for j in range(i * i, rbound, i): 
                """
                the reason for starting from i*i: 
                    all mulitples of 'i' which are less than i*i,are already a multiple of a number less than i
                    multiples of i = i*1, i*2...i*(i-1), i*i....
                """
                isPrime[j] = False
        i+=1
    
    # to find the count of primes, iterate through isPrime
    count = 0
    for _ in range(rbound):
        if isPrime[_]:
            count += 1 
    return count


# print(sieve_of_eratosthenes(2)) # 1
# print(sieve_of_eratosthenes(3)) # 2
# print(sieve_of_eratosthenes(7)) # 4
# print(sieve_of_eratosthenes(19)) # 8
print(sieve_of_eratosthenes(1000)) # 168 # took  0.04779204027727246 ms
