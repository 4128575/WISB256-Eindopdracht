from FiniteFields import *
from ElliptischeKrommen import *
import math
import itertools

def genFieldPol(mod, degree):
    """
    Functie die een willekeurig polynoom van graad n met coefficiënten modulo p genereert.
    """
    ModP = IntegersModP(mod)
    Polynomial = PolynomialSpaceOver(ModP)
 
    while True:
        coefficients = [ModP(random.randint(0, mod-1)) for _ in range(degree)]
        randomMonicPolynomial = Polynomial(coefficients + [ModP(1)])
        return randomMonicPolynomial

def genCurvePoint(kromme):
    """
    Functie die een willekeurig punt op een elliptische kromme over F_p^n genereert.
    """
    mod=kromme.a.prime
    degree=kromme.a.degree
    CurrentField=kromme.a.__class__
    counter=0
    while True:
        counter+=1
        xpol=genFieldPol(mod, degree)
        xpunt=CurrentField(xpol.coefficients)
        kwadraat=kromme.a*xpunt+xpunt**3+kromme.b
        for i in itertools.product(range(mod),repeat=degree):
            ylist=list(i)
            ypunt=CurrentField(ylist)
            if ypunt**2==kwadraat:
                return Punt(kromme, xpunt, ypunt)
        if counter>200:
            raise Exception("Maximum number of iterations exceeded!")

def prime_factors(n):
    """
    Functie die een getal in zijn priemfactoren ontbindt.
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def lcm(a,b):
    """
    Functie die het least common multiple van twee getallen geeft.
    """
    return abs(a * b) / fractions.gcd(a,b) if a and b else 0

def BabyStepGiantStepOnce(kromme):
    """
    Dit algoritme voert het Baby-Step-Giant-Step algoritme één keer uit. Het algoritme begint namelijk met een willekeurig punt en gaat dan verder. Deze functie doet alle stappen
    voor één punt een keer.
    """
    mod=kromme.a.prime
    degree=kromme.a.degree
#    CurrentField=kromme.a.__class__
    randompunt = genCurvePoint(kromme)
#    kwadraat=kromme.a*xpunt+xpunt**3+kromme.b
    m=math.ceil((mod**degree)**(1/4))
    puntlijst=[]
    for j in range(m):
        puntlijst.append(j*randompunt)
    L=1
    Q=(mod**degree+1)*randompunt
    index='unknown'
    tijdelijst=[]
    k=-1
    while True:
        k+=1
        punt2=Q+k*((2*m)*randompunt)
        tijdelijst.append(punt2)
        for j in range(len(puntlijst)):
            if puntlijst[j].x==punt2.x:
                if puntlijst[j].y==punt2.y:
                    index=[-j,k]
                    break
                if puntlijst[j].y==(-punt2).y:
                    index=[j,k]
                    break
            if isinstance(index,list):
                break
        if isinstance(index,list):
            break
    M=int(mod**degree+1+2*m*index[1]+index[0])
    factoren=prime_factors(M)
    factoren=list(set(factoren))
    i=0
    while i < (len(factoren)-1):
        if (M/factoren[i])-int(M/factoren[i])<1.0e-5:
            if (int(M/factoren[i])*randompunt).x=='infx':
                M=int(M/factoren[i])
            else:
                i+=1
    L=lcm(L,M)
    integerlist=list(range((mod**degree)+1-2*math.ceil(math.sqrt(mod**degree)),(mod**degree)+1+2*math.ceil(math.sqrt(mod**degree))))
    counter=0
    N = 'Nothing'
    for integer in integerlist:
        if integer % L == 0:
            N = integer
            counter += 1
    if counter > 1:
        return None
    else:
        return N

def BabyStepGiantStep(kromme):
    """
    Het Baby-Step-Giant-Step algoritme.BSGScheck
    """
    while True:
        resultaat = BabyStepGiantStepOnce(kromme)
        if isinstance(resultaat, int):
            return resultaat

def BSGScheck(kromme):
    """
    Een algoritme dat met brute-force de cardinaliteit van de elliptische kromme over F_p^k berekent om het BSGS algoritme te controleren. Merk op dat dit al gauw veel tijd kost.
    """
    mod=kromme.a.prime
    degree=kromme.a.degree
    CurrentField=kromme.a.__class__
    cardinaliteit = 1
    #vanwege infpoint
    for i in itertools.product(range(mod),repeat=degree):
        ylist=list(i)
        ypunt=CurrentField(ylist)
        for i in itertools.product(range(mod),repeat=degree):
            xlist=list(i)
            xpunt=CurrentField(xlist)
            getal = xpunt**3+kromme.a*xpunt+kromme.b-ypunt**2
            if len(getal.poly) == 1:
                if getal.poly.coefficients[0]==0:
                    cardinaliteit += 1
    return cardinaliteit