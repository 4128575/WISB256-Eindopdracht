import math
import fractions
frac = fractions.Fraction

class ElliptischeKromme(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.check = -16 * (4 * a**3 + 27 * b**2)
        self.discriminant=4 * a**3 + 27 * b**2
        if self.check == 0:
            raise Exception("The curve %s is not smooth!" % self)
            
    def __str__(self):
        return 'y^2=x^3+%sx+%s' % (self.a,self.b)

class Punt(object):
    def __init__(self, kromme, x, y):
        self.kromme = kromme # the curve containing this point
        self.x = x
        self.y = y
        if x**3+self.kromme.a*x+self.kromme.b-y**2>1.0e-5:
            raise Exception("The point %s is not on the given curve %s" % (self, kromme))
    
    def __str__(self):
        return '(%s,%s)' % (self.x,self.y)

    def __neg__(self):
        return Punt(self.kromme, self.x, -self.y)

    def __add__(self,other):
        if isinstance(other, InfPoint):
            return self
        
        if self.x==other.x:
            if self.y==other.y:
                if self.y==0:
                    return InfPoint(self.kromme)
                else:
                    helling=(3*(self.x**2)+self.kromme.a)/(2*self.y)
                    mu=self.y-helling*self.x
                    xcoor=helling**2-2*self.x
                    ycoor=-helling*xcoor-mu
                    return Punt(self.kromme, xcoor, ycoor)
            else:
                return InfPoint(self.kromme)
        else:
            helling=(other.y-self.y)/(other.x-self.x)
            mu=self.y-helling*self.x
            xcoor=helling**2-self.x-other.x
            ycoor=-helling*xcoor-mu
            return Punt(self.kromme, xcoor, ycoor)

    def __mul__(self, n):
        if not isinstance(n, int):
            raise Exception("n needs to be an int!")
        else:
            if n < 0:
                return -self * -n
            if n == 0:
                return InfPoint(self.kromme)
            else:
                binarylijst=bin(n)[2:]
#The number n in binary
                lengte=len(binarylijst)
                binpuntlijst=[self]+[0]*(lengte-1)
#We create a list which starts with the point we are multiplying and has zeros everywhere else.
                for i in range(1,lengte):
                    binpuntlijst[i]=binpuntlijst[i-1]+binpuntlijst[i-1]
#We now have a list that contains P, 2P, 4P, 8P,... 
                binarylijst2=binarylijst[::-1]
#We reverse our binary number to match the positions of P, 2P etc. in our list.
                returnpunt=InfPoint(self.kromme)
                for k in range(lengte):
                    if binarylijst2[k]=='1':
                        returnpunt=returnpunt+binpuntlijst[k]
#We perform the calculation a_0*P+a_1*2P+a_2*4P+a_3*8_+... so that we get n*P.
                return returnpunt
                
    def __rmul__(self, n):
        return self * n
            
    def __sub__(self, other):
        return self +(-other)

class InfPoint(Punt):
    def __init__(self, kromme):
      self.kromme = kromme
      self.x = 'infx'
      self.y = 'infy'
 
    def __str__(self):
        return "Point at infinity"

    def __neg__(self):
        return self

    def __add__(self, other):
        return other
        
    def __mul__(self, n):
        if not isinstance(n, int):
            raise Exception("n needs to be an int!")
        else:
            return self