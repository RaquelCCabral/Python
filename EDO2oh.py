import math
import numpy as np

class EDO():
    def __init__(self, a, b, c, xi, yi, dxi, dyi):
        self.a = a
        self.b = b
        self.c = c
        self.xi = xi
        self.yi = yi
        self.dxi = dxi
        self.dyi = dyi
        self.delta = self.b ** 2 - 4 * self.a* self.c

    def raizes(self):
        if self.delta < 0:
            raiz1 = complex(-self.b, math.sqrt(abs(self.delta)))/(2*self.a)
            raiz2 = complex(-self.b, -math.sqrt(abs(self.delta)))/(2*self.a)
        else:
            if self.delta == 0:
                raiz1 = - self.b/(2*self.a)
                raiz2 = - self.b/(2*self.a)
            else:
                x1 = (- self.b + math.sqrt(self.delta))/(2*self.a)
                x2 = (- self.b - math.sqrt(self.delta))/(2*self.a)  
                if x1 < x2:
                    raiz1 = x2
                    raiz2 = x1
                else:
                    raiz1 = x1
                    raiz2 = x2
        return [raiz1, raiz2]

    def equacao(self):
        if self.delta < 0:
            real = -self.b/(2*self.a)
            imaginaria = (math.sqrt(abs(self.delta)))/(2*self.a)
            y = 'y(x) = e^('+str(real)+'x)(c1.cos('+str(imaginaria)+'x) + c2.sen('+str(imaginaria)+'x)'
        else:
            if self.delta == 0:
                raiz = self.raizes()[0]
                y = 'y(x) = c1.e^('+str(raiz)+'x) + c2.x.e^('+str(raiz)+'x)'
            else:
                raiz1 = self.raizes()[0]
                raiz2 = self.raizes()[1]
                y = 'y(x) = c1.e^('+str(raiz1)+'x) + c2.e^('+str(raiz2)+'x)'
        return y

    def equacaofinal(self):
        if self.delta < 0:
            real = -self.b/(2*self.a)
            imaginaria = (math.sqrt(abs(self.delta)))/(2*self.a)
            A = np.array([[(math.exp(real*self.xi))*math.cos(imaginaria*self.xi), (math.exp(real*self.xi))*math.sin(imaginaria*self.xi)], [(math.exp(real*self.dxi))*((real*math.cos(imaginaria*self.dxi))-(imaginaria*math.sin(imaginaria*self.dxi))), (math.exp(real*self.dxi))*((real*math.sin(imaginaria*self.dxi))+(imaginaria*math.cos(imaginaria*self.dxi)))]])
            B = np.array([self.yi, self.dyi])
            c = np.linalg.solve(A,B)
            c1 = c[0]
            c2 = c[1]
            y = 'y(x) = e^('+str(real)+'x)('+str(c1)+'.cos('+str(imaginaria)+'x) + '+str(c2)+'.sen('+str(imaginaria)+'x)'
        else:
            if self.delta == 0:
                A = np.array([[math.exp((self.raizes()[0])*self.xi), (math.exp((self.raizes()[0])*self.xi))*self.xi], [(math.exp((self.raizes()[0])*self.dxi))*self.raizes()[0], (math.exp((self.raizes()[0])*self.dxi))*(self.raizes()[0]*self.dxi + 1)]])
                B = np.array([self.yi, self.dyi])
                c = np.linalg.solve(A,B)
                c1 = c[0]
                c2 = c[1]
                y = 'y(x) = '+str(c1)+'.e^('+str(self.raizes()[0])+'x) + '+str(c2)+'.x.e^('+str(self.raizes()[0])+'x)'
            else:
                A = np.array([[math.exp((self.raizes()[0])*self.xi), math.exp((self.raizes()[1])*self.xi)], [(math.exp((self.raizes()[0])*self.dxi))*self.raizes()[0], (math.exp((self.raizes()[1])*self.dxi))*self.raizes()[1]]])
                B = np.array([self.yi, self.dyi])
                c = np.linalg.solve(A,B)
                c1 = c[0]
                c2 = c[1]
                y = 'y(x) = '+str(c1)+'.e^('+str(self.raizes()[0])+'x) + '+str(c2)+'.e^('+str(self.raizes()[1])+'x)'
        return y           