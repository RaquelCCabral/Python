# coding=utf-8

import requests
import json
import pyodbc
import pandas as pd

unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
dezena1 = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
dezenas = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
centenas = ['','cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']
milhares = ['', '', 'mil', 'milh', 'bilh', 'trilh']

def numero_valido(n):
    try:
        if len((n)) <= 15:
            x = True
        else:
            x = False
    except ValueError:
        x = False
    return x

def algarismos(n):
    num = n.lstrip('0')
    alg = [int(a) for a in str(num)]
    if alg == []:
        alg = [0, 0, 0]
    return alg

def trio(n):
    x = algarismos(n)
    if len(x) == 1:
        nome = unidades[int(n)]
    elif len(x) == 2:
        d, u = int(x[-2]), int(x[-1])
        if x[-2] == 1:
            nome = dezena1[u]
        else:
            if u!= 0:
                nome = dezenas[d] + ' e ' + unidades[u]
            else:
                nome = dezenas[d]
    else:
        c, d, u = int(x[-3]), int(x[-2]), int(x[-1])
        if u == 0 and d == 0:
            if int(n) == 100:
                nome = 'cem'
            else:
                nome = centenas[c]
        else:
            if u!= 0 and d!= 0:
                if x[-2] == 1:
                    nome = centenas[c] + ' e ' + dezena1[u]
                else:
                    nome = centenas[c] + ' e ' + dezenas[d] + ' e ' + unidades[u]
            elif u == 0:
                nome = centenas[c] + ' e ' + dezenas[d]
            else:
                nome = centenas[c] + ' e ' + unidades[u]
    return nome

def lista_trios(n):
    lista = []
    while len(n)!= 0:
        lista.insert(0, n[-3:])
        n = n[:-3]
    return lista

def escrever(n):
    n = str(n)
    if numero_valido(n) is True:
        lista = lista_trios(n)
        lista_nomes = []
        for i in range(len(lista)):
            classe = milhares[-(i+(6-len(lista)))]
            nome = trio(lista[i]) + ' ' + classe
            if len(trio(lista[i])) == 0:
                nome, classe = '', ''
            if classe in milhares[3:]:
                if int(lista[i]) > 1:
                    nome += 'ões'
                else:
                    nome += 'ão'
            lista_nomes.append(nome)
        while '' in lista_nomes:
            lista_nomes.remove('')
    nome = ', '.join(lista_nomes)
    if int(n) == 1000:
        nome = 'mil'
    return nome.strip()