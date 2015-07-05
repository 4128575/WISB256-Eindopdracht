from FiniteFields import *
from ElliptischeKrommen import *
import math

def genFieldPol(mod, degree):
   ModP = IntegersModP(mod)
   Polynomial = PolynomialSpaceOver(ModP)
 
   while True:
      coefficients = [ModP(random.randint(0, mod-1)) for _ in range(degree)]
      randomMonicPolynomial = Polynomial(coefficients + [ModP(1)])
      return randomMonicPolynomial

def BabyStepGiantStep(kromme):
    mod=kromme.a.prime
    degree=kromme.a.degree
    CurrentField=kromme.a.__class__
    xpol=genFieldPol(mod, degree)
    xpunt=CurrentField(xpol.coefficients)
    return xpunt
        
Mod5=IntegersModP(5)
a=Mod5(3)
irred2=PolynomialSpaceOver(IntegersModP(5))([3,0,1])
F25x = FiniteField(5, 2, irred2)
test=F25x([4])
test2=F25x([3])
curve = ElliptischeKromme(a=F25x([1]), b=F25x([1]))
print(test*a)