def prime_factors(n):
    factors = []
    k = 2

    while k <= n:
        while n % k == 0:
            factors.append(k)
            n //= k
        k += 1

    return factors


def is_half_prime(n):
    factors = prime_factors(n)
    unique_factors = set(factors)

    if len(factors) != len(unique_factors):
        return False

    return len(unique_factors) == 2


boki_trojkatow = []

with open('odcinki.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        line = line.strip()

        boki_trojkata = line.split(' ')
        boki_trojkatow.append(list(map(int, boki_trojkata)))


current_line = 0
max_half_primes_line = 0
max_half_primes = 0
for line in boki_trojkatow:
    a, b, c = line

    how_many_half_primes = int(is_half_prime(a)) + int(is_half_prime(b)) + int(is_half_prime(c))

    if how_many_half_primes > max_half_primes:
        max_half_primes = how_many_half_primes
        max_half_primes_line = current_line

    current_line += 1

print(f'Linia: {max_half_primes_line}')
print(f'Ile: {max_half_primes}')
print(f'Jakie: {boki_trojkatow[max_half_primes_line]}')
