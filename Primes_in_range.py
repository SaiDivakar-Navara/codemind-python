def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True
def count_primes(m,n):
    count = 0
    for num in range(m,n+1):
        if is_prime(num):
            count += 1
    return count
m=int(input())
n=int(input())
count=count_primes(m,n)
print(count)
