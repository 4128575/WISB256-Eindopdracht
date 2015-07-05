from FiniteFields import *
from ElliptischeKrommen import *
import math

def genFieldPol(mod, degree):
    """
    Generate a random polynomial of degree n and coefficients modulo some prime p.
    """
    ModP = IntegersModP(mod)
    Polynomial = PolynomialSpaceOver(ModP)
 
    while True:
        coefficients = [ModP(random.randint(0, mod-1)) for _ in range(degree)]
        randomMonicPolynomial = Polynomial(coefficients + [ModP(1)])
        return randomMonicPolynomial

Mod5=IntegersModP(5)

def BabyStepGiantStep(kromme):
    """
    Rudimentaire versie van Baby-Step-Giant-Step algoritme.
    """
    mod=kromme.a.prime
    degree=kromme.a.degree
    CurrentField=kromme.a.__class__
    q=CurrentField.cardinality
    xpol=genFieldPol(mod, degree)
    xpunt=CurrentField(xpol.coefficients)
    kwadraat=kromme.a*xpunt+xpunt**3+kromme.b
    for k in range(5):
        for l in range(5):
            for u in range(5):
                ypunt=CurrentField([Mod5(k),Mod5(l),Mod5(u)])
                if kwadraat==ypunt**2:
                    print('hoi')
                    return xpunt, ypunt, kwadraat
    return xpunt, ypunt, kwadraat

irred3=PolynomialSpaceOver(IntegersModP(5))([2,1,0,3,1])
irred=PolynomialSpaceOver(IntegersModP(5))([4,3,1,1])
irred2=PolynomialSpaceOver(IntegersModP(5))([3,0,1])
F35x = FiniteField(5, 3, irred)
F25x = FiniteField(5, 2, irred2)
F45x = FiniteField(5, 4, irred3)
curve = ElliptischeKromme(a=F25x([1]), b=F25x([1]))
curve2 = ElliptischeKromme(a=F35x([1]), b=F35x([1]))
curve3 = ElliptischeKromme(a=F45x([1]), b=F45x([1]))

xwerk=PolynomialSpaceOver(IntegersModP(5))([1,4,2,4])
ywerk=PolynomialSpaceOver(IntegersModP(5))([0,0,1,0])

def BabyStepGiantStep2(kromme,x,y):
    mod=kromme.a.prime
    degree=kromme.a.degree
    CurrentField=kromme.a.__class__
    q=CurrentField.cardinality
    xpunt=CurrentField(x.coefficients)
    ypunt=CurrentField(y.coefficients)
    kwadraat=kromme.a*xpunt+xpunt**3+kromme.b-ypunt**2
    punt=Punt(kromme,xpunt,ypunt)
    getal=math.ceil((mod**degree)**(1/4))
    m = getal+1
    puntlijst=[]
    for j in range(m):
        puntlijst.append(j*punt)
    L=1
    Q=(mod**degree+1)*punt
    k=0
    infloop=0
    index='unknown'
    while True:
        punt2=Q+k*((2*m)*punt)
        for j in range(len(puntlijst)):
            if puntlijst[j]==punt2:
                index=-j
                break
            if puntlijst[j]==-punt2:
                index=j
                break
        k+=1
        infloop+=1
        if infloop==100:
            break
    return punt2

print(BabyStepGiantStep2(curve3,xwerk,ywerk))


"""
 a=0
    while True:
        a+=1
        ypol=genFieldPol(mod, degree)
        ypunt=CurrentField(ypol.coefficients)
        if a==100:
            break
        if ypol*ypol==kwadraat:
            print('hoi')
            break
"""