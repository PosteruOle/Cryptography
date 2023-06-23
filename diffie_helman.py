import random
from copy import deepcopy

def mod_pow(a, n, m):
    a = a % m
    result = 1
    while n > 0:
       if n % 2 == 1:
          result = (result * a) % m
       a = (a * a) % m
       n = n // 2
    return result

def extended_gcd(a, b):
    if b == 0:
       return (a, 1, 0)
    d, m, n = extended_gcd(b, a % b)
    return (d, n, m - a // b * n)

def mod_inv(a, x):
    d, m, n = extended_gcd(a, x)
    if d != 1:
       print("Vrednosti a i x nisu uzajamno proste!")
    else:
       return m % x    

def miller_rabin(n, k):
    if n <= 3:
       if n == 1:
          return False
       return True

    d = n - 1
    r = 0
    while d % 2 == 0:
       r = r + 1
       d = d // 2
    for i in range(k):
       a = random.randrange(2, n - 1)
       x = mod_pow(a, d, n)
       
       if x == 1 or x == n - 1:
          continue
       
       witness = True
       
       for j in range(r - 1):
           x = mod_pow(x, 2, n)
           if x == 1:
              return False
           if x == n - 1: # n - 1 = -1 (mod n)
              witness = False
              break
       if witness:
          return False
    return True

def get_prime(limit, k = 20):
    is_prime = False
    while not is_prime:
        n = random.randrange(limit)
        is_prime = miller_rabin(n, k)
    return n

class Diffie_Helman:
    def __init__(self, q, g):
        self.q=q
        self.g=g
        self.private_key=random.randradnge(2, self.q)
        self.public_key=mod_pow(self.g, self.private_key, self.q)
    
    def get_key(self, pub_key):
        return mod_pow(pub_key, self.private_key, self.q)


def main():
    limit = 2 ** 256
    q = get_prime(limit)
    g = random.randrange(2, q)
    A = Diffie_Helman(q, g)
    B = Diffie_Helman(q, g)
    
    print(A.private_key, A.public_key)
    print(B.private_key, B.public_key)
    
    print(A.get_key(B.public_key))
    print(B.get_key(A.public_key))


if __name__=="__main__":
   main()
