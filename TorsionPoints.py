from FiniteFields import *
from ElliptischeKrommen import *
import math


def Cardano(a, b):
    """
    functie die de reële oplossingen van x^3+a*x+b=0 geeft.
    """
    
    if a == 0:
        if b == 0:
            return [0]
        else:
            x1 = (-b)**(1/3)
            x2 = ((-1)**(1/3)) * (b)**(1/3)
            x3 = -((-1)**(2/3)) * (b)**(1/3)
            filtered = [i.real for i in [x1, x2, x3] if abs(i.imag) < 1.0e-5]
            
            return filtered
            
    if b == 0:
        x1 = 0
        x2 = (-a)**(1/2)
        x3 = -(-a)**(1/2)
        filtered = [i.real for i in [x1, x2, x3] if abs(i.imag) < 1.0e-5]
        
        return filtered
        
    R = -b / 2
    Q = a / 3
    K1 = (R + (R**2 + Q**3)**(1/2))**(1/3)
    x1 = K1 - a / (3 * K1)
    x2 = (-(-1)**(1/3) * K1) - a/(3 * (-(-1)**(1/3) * K1))
    x3 = ((-1)**(2/3) * K1) - a / (3 * ((-1)**(2/3) * K1))
    filtered = [i.real for i in [x1, x2, x3] if abs(i.imag) < 1.0e-5]
    
    return filtered

def FindTorsionPoints(kromme):
    """
    Functie die de torsiepunten van een elliptische kromme over Q vindt.
    Allereerst vinden we alle punten (x,0) (deze punten hebben orde 2).
    """
    
    xopl = []
    
    for x in Cardano(kromme.a, kromme.b):
        if abs(x - round(x)) < 1.0e-7:
            xopl.append(round(x))
            
    orde2lijst = [Punt(kromme, xw, 0) for xw in xopl]
    
    """
    Nu vinden we y ongelijk aan nul in Z zodat y^2|D.
    """
    
    D = kromme.discriminant
    ylijst = []
    
    for i in range(1, int(abs((D)**(1/2))) + 2):
        if D % (i**2) == 0:
            ylijst.append(i)
            
    """
    Nu willen we roots van y^2=x^3+a*x+b vinden. Hiervoor gebruiken we Cardano's methode.
    """
    
    punten = []
    
    for y in ylijst:
        xwaarden = []
        
        for x in Cardano(kromme.a, kromme.b - y**2):
            if abs(x - round(x)) < 1.0e-7:
                xwaarden.append(round(x))
                
        for x in xwaarden:
            punten.append([x, y])
            punten.append([x, -y])
            
    torsiepunten = []
    
    for punt in punten:
        rekenpunt = Punt(kromme, punt[0], punt[1])
        
        if isinstance((12 * rekenpunt), InfPoint):
            torsiepunten.append(rekenpunt)
        else:
            for i in [5, 7, 8, 9]:
                if isinstance((i*rekenpunt),InfPoint):
                    torsiepunten.append(rekenpunt)
                    
                    break
                
    for punt in orde2lijst:
        torsiepunten.append(punt)
        
    torsiepunten.append(InfPoint(kromme))
    
    return torsiepunten

def GroupStructure(kromme, torsiepuntlijst = None):
    """
    Functie die de groepsstructuur van de torsiegroep geeft.
    """
    
    if torsiepuntlijst == None:
        torsiepunten = FindTorsionPoints(kromme)
    else:
        torsiepunten = torsiepuntlijst
        
    cardinaliteit = len(torsiepunten)
    
    if cardinaliteit in [1, 2, 3, 5, 6, 7, 9, 10]:
        return "E_tors" ' \u2245 ' + 'Z/%dZ' % (cardinaliteit)
        
    if cardinaliteit == 16:
        return "E_tors" ' \u2245 ' + 'Z/2Z x Z/8Z'
        
    if cardinaliteit == 4:
        for punt in torsiepunten:
            if not isinstance((2 * punt), InfPoint):
                return "E_tors" ' \u2245 ' + 'Z/%dZ' % (cardinaliteit)
                
        return "E_tors" ' \u2245 ' + 'Z/2Z x Z/2Z'
        
    if cardinaliteit == 8:
        for punt in torsiepunten:
            if not isinstance((4 * punt), InfPoint):
                return "E_tors" ' \u2245 ' + 'Z/%dZ' % (cardinaliteit)
                
        return "E_tors" ' \u2245 ' + 'Z/2Z x Z/4Z'
        
    if cardinaliteit == 12:
        for punt in torsiepunten:
            if not isinstance((6 * punt), InfPoint):
                if not isinstance((4 * punt), InfPoint):
                    return "E_tors" ' \u2245 ' + 'Z/%dZ' % (cardinaliteit)
                    
        return "E_tors" ' \u2245 ' + 'Z/2Z x Z/8Z'