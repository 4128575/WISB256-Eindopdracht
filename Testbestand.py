from FiniteFields import *
from ElliptischeKrommen import *
from BSGS import *
from TorsionPoints import *
import math


print("""
Eerst testen we de functionaliteiten omtrent de eindige lichamen. We beginnen met het standaard polynoom rekenen over Q.

-Polynoom Rekenen:
Polynoom definities. Merk op dat overbodige nullen (op het eind) worden weggehaald, ook wordt 1*x^k als x^k weergegeven.
""")

Pols = PolynomialSpaceOver()
fun1 = Pols([1, 2, 3])
fun2 = Pols([1, 2])
fun3 = Pols([1, 4, 5])
fun4 = Pols([1, 4, 4])
fun5 = Pols([1, 2, 8, 0, 0])
fun6 = Pols([63, 4, 1, 0, 0, 10, 234, 324, 1, 9])
fun7 = Pols([1, 4, 5])
fun8 = Pols([1, 2, 8])
fun0 = Pols([0])
fun9 = Pols([2, 7])
fun10 = Pols([6, 35, 81, 144, 112])
fun11 = Pols([1, 1, 4])
fun12 = Pols([6, 29, 28])
print(fun1,'   ', fun2,'   ', fun3,'   ', fun4,'   ', fun5,'   ', fun6,'   ', fun7,'   ', fun8,'   ', fun0)

print("""
-Polynoom Operaties:
Allereerst gelijkheid van polynomen, merk op dat het niet hetzelfde object hoeft te zijn en dat de nullen geen invloed hebben.
""")

print(fun6 == fun6, fun1 == fun2, fun1 == fun3, fun1 == fun4, fun3 == fun7, fun5 == fun8, fun0 == fun1)

print("""
Optellen en aftrekken van polynomen gaat op de gebruikelijke manier.
""")

print(fun1 + fun3,'   ', fun1 + fun2,'   ', fun3 + fun4,'   ', fun6 + fun8,'   ', fun1 - fun2,'   ', -fun3 + fun6,'   ', fun1 + fun0)

print("""
Vermenigvuldiging gaat op de gebruikelijke manier met distributiviteit etc.
""")

print(fun2 * fun4,'   ', fun3 * fun3,'   ', fun1 * fun3,'   ', fun4 * fun4,'   ', fun6 * fun6,'   ', fun8 * fun2,'   ', fun0 * fun6)

print("""
Staartdeling geeft het quotiënt en de rest terug. Longdiv werkt op lijsten en niet op polynomen en wordt dus bij deling op de coefficienten lijst losgelaten.
Delen door nul gaat niet. Deze tuple van 2 lijsten stelt dus het quotiënt polynoom en het rest polynoom voor.
""")

testdiv1 = [1, 2]
testdiv2 = [2, 3, 2]
testdiv3 = [4, 5, 1, 2]
testdiv4 = [8]
testdiv0 = [0]
print(longdiv(testdiv2, testdiv1),"   ", longdiv(testdiv3, testdiv1),"   ", longdiv(testdiv3, testdiv2),"   ", longdiv(testdiv3, testdiv4),"   ", longdiv(testdiv0, testdiv4))

print("""
Met longdiv kunnen we divmod definiëren.
""")

print(divmod(fun1, fun3),"   ", divmod(fun5, fun3),'   ', divmod(fun6, fun5),'   ', divmod(fun2, fun1),'   ', divmod(fun6, fun3))

print("""
En deling, dit werkt alleen wanneer de noemer een factor is van de teller.
""")

print(fun4 / fun2,"   ", fun10 / fun9,"   ", fun10 / fun11,"   ", fun10 / fun12,"   ", fun9 / fun9)

print("""
Nu even kort dat het modulo rekenen werkt naar behoren. Merk op dat wanneer men elementen van mod p en mod k combineert het rekenen modulo het linker element gaat.

Modulo operaties en representaties.
""")

Mod5 = IntegersModP(5)
Mod11 = IntegersModP(11)
Mod23 = IntegersModP(23)
Mod53 = IntegersModP(53)
Mod8677 = IntegersModP(8677)
print([Mod53(33)],'   ', Mod53(33),'   ', Mod5(3) + Mod5(11),'   ', Mod5(7) * Mod5(3),'   ', Mod5(3) * Mod53(2),'   ', Mod53(3) * Mod5(2),'   ', Mod53(23) / Mod53(2),'   ',Mod8677(5643) / Mod8677(123),'   ', Mod53(12) - Mod53(27),'   ', Mod5(2) == Mod5(2),'   ', Mod53(2) == Mod5(2),'   ', Mod53 > Mod53(12))

print("""
Irreducibles werken naar behoren binnen Finite Fields en het Extended Euclidean Algorithm voor polynomen ook.
""")

PolyOverQ = PolynomialSpaceOver().factory
polysMod5 = PolynomialSpaceOver(Mod5).factory
polysMod11 = PolynomialSpaceOver(Mod11).factory

randomMonicPolynomial = PolynomialSpaceOver(Mod23)([Mod23(random.randint(0, 23 - 1)) for _ in range(3)] + [Mod23(1)])
irred = PolynomialSpaceOver(IntegersModP(5))([4, 3, 1, 1])
irred2 = PolynomialSpaceOver(IntegersModP(5))([3, 0, 1])
irred3 = PolynomialSpaceOver(IntegersModP(5))([2, 1, 0, 3, 1])
irred4 = PolynomialSpaceOver(IntegersModP(5))([1, 7, 49])
fun6e = PolynomialSpaceOver(IntegersModP(5))([63, 4, 1, 0, 0, 10, 234, 324, 1, 9])
c = PolyOverQ([1, 4, 4])
d = PolyOverQ([1, 2])

print(Reducible(irred4, 5), Reducible(irred, 5), Reducible(fun6e, 5), Reducible(irred2, 5), Reducible(irred3, 5), gcdpol(c, d),'   ', randomMonicPolynomial,'   ', Reducible(randomMonicPolynomial, 23),'   ', genIrreduciblePoly(23, 3))

print("""
Het rekenen met Polynoom elementen van graad n met coëfficiënten modulo p.
""")

print(PolyOverQ([1, 7, 49]) / PolyOverQ([7]),'   ', polysMod5([1, 6, 2, 4, 7, 1]),'   ', polysMod5([1, 7, 49]) / polysMod5([7]),'   ', polysMod11([1, 7, 49]) / polysMod11([7]),'   ', polysMod5([1, 6, 2, 4, 7, 1])**2,'   ', polysMod11([1, 7, 49]) + polysMod11([1, 7, 49]),'   ', polysMod5([1, 7, 49])**2)

print("""
Het rekenen met Finite Fields F_(p^n). We kunnen optioneel een irreducibel polynoom meegeven. Als we dit niet doen wordt er automatisch een gegenereerd. 
De operaties werken zoals het hoort (zie de vergelijking met polynomen mod p). Merk op dat in een eindig lichaam de uitkomst van een operatie uiteindelijk modulo een irreducibel polynoom gaat.
""")

F23 = FiniteField(2, 3)
irred = PolynomialSpaceOver(IntegersModP(2))([1, 0, 1, 1])
F23x = FiniteField(2, 3, irred)
ub = F23([1, 1])
uc = F23x([1, 1])
print(ub,"  ", ub * ub,"  ", ub.inverse(),"  ", uc,"  ", uc**10,"  ", uc * uc.inverse(),'   ', F23.generator)

irred5 = polysMod5([4, 2, 1])
F25x = FiniteField(5, 2, irred5)
x = F25x([2, 1])
y = F25x([0, 1])
tes1 = polysMod5([2, 1])
tes2 = polysMod5([0, 1])
print(tes1 * tes2,"  ", (tes1 * tes2) % irred5," |", tes2**2,"  ", (tes2**2) % irred5,"    |", tes1**3,"  ", (tes1**3) % irred5,"|", tes1*(tes2**2),"  ", (tes1*(tes2**2)) % irred)
print(x * y,"   |", y**2,"|", x**3,"            |", x * (y**2))

print("""
Tenslotte laten we zien dat deze classes ook met elkaar gebruikt kunnen worden. Merk op dat niet alle operaties tussen alle verschillende classes zullen werken maar wel
de benodigde voor dit project.
""")

print(Mod5(2) * 2,'   ', 12 * Mod53(6),'   ', Mod5(2)**3,'   ', Mod53(12) / 12,'   ', 12 * tes1,'   ', 4 * x,'   ', 12 + x,'   ', x / 2,'   ', x / Mod5(2))

print("""
We kunnen uiteraard ook Elliptischekrommen definiëren, zowel over Q als over F_(p^n), en hier operaties op uitvoeren.
""")

testkromme = ElliptischeKromme(frac(-2), frac(4))
testkromme2 = ElliptischeKromme(frac(1), frac(2))
testp1 = Punt(testkromme, frac(3), frac(5))
testp2 = Punt(testkromme, frac(-2), frac(0))
testp3 = Punt(testkromme2, frac(-1), frac(0))
testp4 = Punt(testkromme2, frac(0), frac(2))
print(testp2 + testp1, testp2 + testp2, -testp1, testp1 * 5, 5 * testp1, testp2 - 3 * testp1, testp3 * 5, testp3 * 10, testp3 - testp4)

F5 = FiniteField(5, 1)
C1 = ElliptischeKromme(a = F5(1), b = F5(1))
P1 = Punt(C1, F5(2), F5(1))
print(P1,"  ", 2 * P1,"  ", 3 * P1)

curve = ElliptischeKromme(a = F25x([1]), b = F25x([1]))
x2 = F25x([2, 1])
y2 = F25x([1, 2])
P2 = Punt(curve, x2, y2)
print(P2,"   ", -P2,"   ", 2 * P2,"   ", 4 * P2,"   ", 9 * P2)

irred6 = polysMod11([8, 7, 9, 7, 5, 2, 9, 1])
F117x = FiniteField(11, 7, irred6)
curve2 = ElliptischeKromme(F117x([4, 2, 2]), F117x([6, 10, 3, 3, 0, 3, 2]))
x3 = F117x([8, 2, 4])
y3 = F117x([0, 1])
P3 = Punt(curve2, x3, y3)

print(P3,'    ', P3 * 4,'    ', P3 * 24,'   ', P3 * 10000)

print("""
Over Q kunnen we de punten met eindige orde (torsiepunten) bepalen en de groepsstructuur weergeven.
""")

testkromme = ElliptischeKromme(-43, 166)
a = FindTorsionPoints(testkromme)

print("Voor: ", testkromme)

for i in range(len(a)):
    print(a[i])
    
print(GroupStructure(testkromme), "\n")

testkromme = ElliptischeKromme(14, 19)
a = FindTorsionPoints(testkromme)

print("Voor: ", testkromme)

for i in range(len(a)):
    print(a[i])
    
print(GroupStructure(testkromme), "\n")

testkromme = ElliptischeKromme(1, 2)
a = FindTorsionPoints(testkromme)

print("Voor: ", testkromme)

for i in range(len(a)):
    print(a[i])
    
print(GroupStructure(testkromme), "\n")

testkromme = ElliptischeKromme(2, 0)
a = FindTorsionPoints(testkromme)

print("Voor: ", testkromme)

for i in range(len(a)):
    print(a[i])
    
print(GroupStructure(testkromme), "\n")

testkromme = ElliptischeKromme(-4, 0)
a = FindTorsionPoints(testkromme)

print("Voor: ", testkromme)

for i in range(len(a)):
    print(a[i])
    
print(GroupStructure(testkromme), "\n")

print("""
Tenslotte hebben we het Baby-Step-Giant-Step algoritme geïmplementeerd over F_(p^k). Hiermee vinden we de cardinaliteit van Elliptische Krommen over F_(p^k). Dit berekenen duurt best lang,
hoewel niet zolang als puur brute-forcen, omdat er telkens een willekeurig punt gevonden moet worden en dit gaat deels op een bruteforce manier. Bijgeleverd is ook een "BSGS" checkalgoritme.
Hiermee vinden we domweg de cardinaliteit van de kromme door alle mogelijke combinaties van punten af te gaan. Hiermee kan je controleren dat het algoritme inderdaad functioneert.
De code staat op het moment uit omdat het erg lang duurt (zeker de laatste kromme). Ter informatie, voor de eerste kromme geeft het check algoritme 27, de tweede 108 en de derde 675.
""")

irred7 = PolynomialSpaceOver(IntegersModP(5))([2, 1, 0, 3, 1])
irred8 = PolynomialSpaceOver(IntegersModP(5))([4, 3, 1, 1])
irred9 = PolynomialSpaceOver(IntegersModP(5))([3, 0, 1])
F35xe = FiniteField(5, 3, irred8)
F25xe = FiniteField(5, 2, irred9)
F45xe = FiniteField(5, 4, irred7)
kromme = ElliptischeKromme(a = F25xe([1]), b = F25xe([1]))
kromme2 = ElliptischeKromme(a = F35xe([1]), b = F35xe([1]))
kromme3 = ElliptischeKromme(a = F45xe([1]), b = F45xe([1]))

resultaat = BabyStepGiantStep(kromme)
#resultaat2 = BabyStepGiantStep(kromme2)
#resultaat3 = BabyStepGiantStep(kromme3)
print(resultaat)
#print(resultaat2)
#print(resultaat3)
#print(BSGScheck(kromme),BSGScheck(kromme2))