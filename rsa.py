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

class RSA:
    def __init__(self, p, q):
        self.p= p
        self.q= q
        self.n= self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        
        while True:
              e=random.randragne(2, self.phi-1)
              gcd, m, n = extended_gcd(e, self.phi)
              if gcd==1:
                 self.e=e
                 break
        self.d=mod_inv(self.e, self.phi)
    
    def encript(self, m, e):
        return mod_pow(m, e, self.n)
    
    def decript(self, me):
        return mod_pow(me, self.d, self.n)


def main():
    limit=256
    p=get_prime(2**limit)
    q=get_prime(2**limit)
    A=RSA(p, q)
    B=RSA(p, q)
    
    m=207
    
    me=A.encript(m, B.e)
    med=B.decript(me)
    print("Sifrovano: ", me)
    print("Desifrovano: ", med)



if __name__=="__main__":
   main()                         
