def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b%a, a)
        return (g, x-(b//a)*y, y)

def IntegersModP(p):
    class IntegerModP(object):
        def __init__(self, n):
            self.n = n % p
            self.field = IntegerModP
            self.p=p
        
        def __neg__(self): 
            return IntegerModP(-self.n)
        
        def __str__(self): 
            return str(self.n)
        
        def __add__(self, other):
            return IntegerModP(self.n + other.n)
            
        def __sub__(self, other): 
            return IntegerModP(self.n + (-other.n))
 
        def __mul__(self, other): 
            return IntegerModP(self.n * other.n)
        
        def __eq__(self, other): 
            if self.n==other.n and isinstance(other, IntegerModP)==True:
                return True
            else:
                return False
        
        def __abs__(self): 
            return abs(self.n)
        
        def __repr__(self): 
            return '%d (mod %d)' % (self.n, self.p)
            
        def __divmod__(self, div):
            geheel=divmod(self.n,div.n)[0]
            remainder=divmod(self.n,div.n)[1]
            return (IntegerModP(geheel), IntegerModP(remainder))
            
        def modinverse(self):
            gcd, x, y = egcd(self.n, self.p)
            if gcd != 1:
                return None  # modular inverse does not exist
            else:
                return x % self.p

        def __truediv__(self, other): 
            return self * other.modinverse()
            
        def __div__(self, other): 
            return self * other.modinverse()
    IntegerModP.p = p
    IntegerModP.__name__ = 'Z/%d' % (p)
    return IntegerModP