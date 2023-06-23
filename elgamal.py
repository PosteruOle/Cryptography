class ElGamal:
    def __init__(self, q, g):
        self.q=q
        self.g=g
        self.pr=random.randrange(2, self.q) 
        self.pub=mod_pow(self.g, self.pr, self.q)
        
     def encrypt(self, m, pub_key):
         k=random.randrange(2, self.q)
         g_k=mod_pow(self.g, self.k, self.q)
         e=mod_pow(g_k, pub_key, self.q)
         me=(m * e) % self.q
         return (me, g_k)
     
     def decrypt(self, me, g_k):   
         e=mod_pow(g_k, self.pr, self.q)
         d=mod_inv(e, self.q)
         m=(me*d)%self.q
         
         return m


def main():
    q=get_prime(2**256)
    g=random.randrange(2, q)
    A=ElGamal(q, g)
    B=ElGamal(q, g)
    
    m=...
    
    ()


if __name__=="__main__":
   main()
