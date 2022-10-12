import sympy
from sympy import *
import numpy as np
import pandas as pd

x = sympy.Symbol('x')

def fx(funcao, valores_x):
    resultado = []
    for i in range (len(valores_x)):
        resultado.append(funcao.subs({x:valores_x[i]}))
    return resultado

def interpolacao_linear(ponto1, ponto2):
    a0,a1 = sympy.symbols('a0 a1')
    p0 = sympy.Eq(a1*ponto1[0]  + a0, ponto1[1])
    p1 = sympy.Eq(a1*ponto2[0]  + a0, ponto2[1])
    resultado = sympy.solve((p0, p1), (a1, a0))
    return print('P(x) = ', resultado[a1]*x + resultado[a0])

def interpolacao_quadratica(ponto1, ponto2, ponto3):
    a0,a1,a2 = sympy.symbols('a0 a1 a2')
    p0 = sympy.Eq(a2*(ponto1[0])**2  + a1*ponto1[0] + a0, ponto1[1])
    p1 = sympy.Eq(a2*(ponto2[0])**2  + a1*ponto2[0] + a0, ponto2[1])
    p2 = sympy.Eq(a2*(ponto3[0])**2  + a1*ponto3[0] + a0, ponto3[1])
    resultado = sympy.solve((p0, p1, p2), (a2, a1, a0))
    return print('P(x) = ', resultado[a2]*x**2 + resultado[a1]*x + resultado[a0])

def interpolacao_lagrange(listax, listafx):
    L = []
    Lnum = []
    Lden = []
    i = 0
    while i < len(listax):
        j = 0
        numeradores = []
        denominadores = []
        while j < len(listax):
            if j == i:
                numerador = 1
                denominador = 1
            else:
                numerador = x - listax[j]
                denominador = listax[i] - listax[j]
            numeradores.append(numerador)
            denominadores.append(denominador)
            j += 1
        Lnum.append(sympy.expand(prod(numeradores)))
        Lden.append(prod(denominadores))
        i+= 1

    for n,d in zip(Lnum, Lden):
        L.append(n/d)

    resultado = sum(np.multiply(listafx, L))
    return print('P(x) = ', resultado)

def interpolacao_newton(listax, listafx, ponto = None, n = None):
    df = pd.DataFrame()
    s = 'Ordem 0'
    df['x'] = listax
    df[s] = listafx
    j = 0
    while j < (len(df[s])-1):
        i = 0
        ordem = []
        num = int(s[len(s)-1]) + 1
        while i < (len(df[s]) - 1):
            try:
                elemento = (df[s][i+1] - df[s][i])/(df['x'][i+num] - df['x'][i])
                ordem.append(elemento)
            except KeyError: None
            i += 1
        while len(ordem) < len(df):
            ordem.append(None)
        s = s.replace(s[len(s) - 1], str(num))
        df[s] = ordem
        j += 1
    x = sympy.Symbol('x')
    f = list(df.loc[0])[1:]
    xi = [1]
    P = []
    for k in range(len(df)):
        xi.append((x - df['x'][k]))
    xn = xi[:(n+1)]
    for p in range(len(f)):
        P.append(f[p]*prod(xn[:p+1]))
    return print('P(x) = ',sum(P), '/nP(x) = ', sympy.expand(sum(P)))
    return df