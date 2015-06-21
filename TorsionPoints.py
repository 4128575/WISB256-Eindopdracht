from FiniteFields import *
from ElliptischeKrommen import *
import math

def Cardano(a,b):
    """
    functie die de reële oplossingen van x^3+a*x+b=0 geeft.
    """
    R=-b/2
    Q=a/3
    K1=(R+(R**2+Q**3)**(1/2))**(1/3)
    x1=K1-a/(3*K1)
    x2=(-(-1)**(1/3)*K1)-a/(3*(-(-1)**(1/3)*K1))
    x3=((-1)**(2/3)*K1)-a/(3*((-1)**(2/3)*K1))
    filtered = [i.real for i in [x1,x2,x3] if abs(i.imag) < 1.0e-5]
    return filtered

def FindTorsionPoints(kromme):
    """
    Functie die de torsiepunten van een elliptische kromme over Q vindt.
    Allereerst vinden we alle punten (x,0) (deze punten hebben orde 2).
    """
    xopl=[]
    for x in Cardano(kromme.a,kromme.b):
        if abs(x-int(x))<1.0e-7:
            xopl.append(x)
    orde2lijst=[Punt(kromme,xw,0) for xw in xopl]
    """
    Nu vinden we y ongelijk aan nul in Z zodat y^2|D.
    """
    D=kromme.discriminant
    ylijst=[]
    for i in range(1,abs(int((D)**(1/2)))+2):
        if D % (i**2)==0:
            ylijst.append(i)
    """
    Nu willen we roots van y^2=x^3+a*x+b vinden. Hiervoor gebruiken we Cardano's methode.
    """
    punten=[]
    for y in ylijst:
        xwaarden=Cardano(kromme.a,kromme.b-y**2)
        for x in xwaarden:
            punten.append([x,y])
            punten.append([x,-y])
    torsiepunten=[]
    for punt in punten:
        rekenpunt=Punt(kromme,punt[0],punt[1])
        if 12*rekenpunt==InfPoint(kromme):
            torsiepunten.append(rekenpunt)
        else:
            for i in [5,7,8,9]:
                if i*rekenpunt==InfPoint(kromme):
                    torsiepunten.append(rekenpunt)
                    break
    for punt in orde2lijst:
        torsiepunten.append(punt)
    torsiepunten.append(InfPoint(kromme))
#    testpunt=Punt(kromme,punten[0][0],punten[0][1])
#    nplijst=[i*testpunt for i in range(2,11)]
#    nplijst.append(12*testpunt)
    return torsiepunten

testkromme = ElliptischeKromme(frac(2),frac(4))
a=FindTorsionPoints(testkromme)
#for i in range(len(a[0])):
#    print(a[0][i])
print(a[0])