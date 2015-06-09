import math

class ElliptischeKromme(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.check = -16 * (4 * a**3 + 27 * b**2)
        if self.check == 0:
            print('Exception: The curve %s is not smooth!' % self)
#hier moeten we het programma een foutmelding laten geven (en dus het programma stop zetten) en niet alleen een melding!
            
    def __str__(self):
        return 'y^2=x^3+%sx+%s' % (self.a,self.b)

curvegoed=ElliptischeKromme(1,2)
curvefout=ElliptischeKromme(0,0)

class Punt(object):
    def __init__(self, kromme, x, y):
        self.kromme = kromme # the curve containing this point
        self.x = x
        self.y = y
        if y**2!=x**3+self.kromme.a*x+self.kromme.b:
            print('Exception: The point %s is not on the given curve %s' % (self, self.kromme))
#hier moeten we het programma een foutmelding laten geven (en dus het programma stop zetten) en niet alleen een melding!
    
    def __str__(self):
        return '(%s,%s)' % (self.x,self.y)

    def __neg__(self):
        return Punt(self.kromme, self.x, -self.y)

#Ik heb nog moeite met deze methode. We moeten hier sowiezo apparte gevallen onderscheiden voor als ze dezelfde x-coordinaat hebben. Tot dusver heb ik dit.
    def __add__(self,other):
        slope=(other.y-self.y)/(other.x-self.x)
        p=(slope**2)/3
        r=(self.kromme.a-2*slope*(self.y-slope*self.x))/3
        q=p**3+((2*slope*(self.y-slope*self.x)-self.kromme.a)*(slope**2)-3*(self.kromme.b-(self.y-slope*self.x)**2))/6
        xcoor=(q+math.sqrt(q**2+(r-p**2)**3))**(1/3)+(q-math.sqrt(q**2+(r-p**2)**3))**(1/3)+p
        ycoor=self.y+slope*(xcoor-self.x)
        return Punt(self.kromme, xcoor, -ycoor)
        

puntgoed=Punt(curvegoed,1,2)
puntfout=Punt(curvegoed,1,1)

testkromme = ElliptischeKromme(-2,4)
testp1 = Punt(testkromme, 3, 5)
testp2 = Punt(testkromme, -2, 0)
print(testp1+testp2)