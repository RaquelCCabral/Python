import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

def alturas(n):
    x = st.norm.rvs(loc = 1.7, scale = 0.08, size = n) # np.ndarray com n alturas aleatórias
    fig, axs = plt.subplots()
    axs.hist(x, bins=20) # Criando o histograma
    axs.set_title('Alturas') # Adicionando o título
    plt.savefig('alturas.png') # Salvando a figura
    plt.show()
    return x

def pesos(alturas):
    m = len(alturas)
    imc = st.norm.rvs(loc = 24.5, scale = 4.3, size = m) # IMC
    fig, axs = plt.subplots()
    pesos = imc*(alturas**2) # Calculo do peso
    axs.hist(pesos, bins=20) # Criando o histograma
    axs.set_title('Pesos') # Adicionando o título
    plt.savefig('pesos.png') # Salvando a figura
    plt.show()
    return pesos

def regressaoLinear(alturas, pesos):
    fig, ax = plt.subplots()
    a = st.linregress(alturas, pesos).slope # Encontro a
    b = st.linregress(alturas, pesos).intercept # Encontro b
    x = alturas
    y = a*x + b # Relação linear dos pesos em relação as alturas dadas e os parâmetros encontrados
    ax.plot(x, y, 'r-') # Plotando a reta
    plt.xlabel('Altura') # Rótulo do eixo x
    plt.ylabel('Peso') # Rótulo do eixo y
    plt.scatter(alturas, pesos) # Plotando a dispersão de dados
    ax.set_title('Altura vs. Peso') # Adicionando o título
    plt.savefig('regressao.png') # Salvando a figura
    plt.show()
    return (a, b)        