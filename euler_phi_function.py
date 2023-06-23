def factorize(n):
    if n <= 3:
       return [n]
    factors = []
    
    while n % 2 == 0:
          factors.append(2)
          n = n // 2
    i = 3
    while  n > 1:
        if n % i==0:
           factors.append(i)
           n = n // i          
        else:
           i = i + 2
    return factors
           
def phi(n):
    factors=set(factorize(n))
    res = 1
    
    for factor in factors:
        n = n // factor
        res = res * (factor - 1)
    return n * res      

def main():
    n = int(input("Unesite ceo broj n: "))
    print("phi(n) = ", phi(n))

if __name__=="__main__":
   main()
