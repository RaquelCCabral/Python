import numpy as np
import matplotlib.pyplot as plt

def racional(n):
    fig, ax = plt.subplots(figsize = (6, 6)) # Quadro de tamanho 6x6 e frame
    x = np.linspace(0.1, 2, n) # n pontos no intervalo [0.1, 2]
    y = 1/x
    ax.plot(x, y, 'c-s', linewidth = 2, label = '$y = 1/x$') # Plotando gráfico 1/x
    y = 1/(x**2)
    ax.plot(x, y, 'm-o', linewidth = 2, label = '$y = 1/x²$') # Plotando gráfico 1/x²
    ax.legend(loc = 'upper right') # Localização dos rótulos das funções
    ax.set_title('Funções racionais') # Título
    ax.set_xticks([0, 1, 2]) # Números no eixo x
    plt.show()
    return None

def polinomios(n):
    fig, ax = plt.subplots(figsize = (6, 6)) # Quadro de tamanho 6x6 e frame
    x = np.linspace(-1, 1, 100) # 100 pontos no intervalo [-1, 1]
    for i in range(n):
        y = x**(i+1) # uso i+1 pois o range começa no 0
        ax.plot(x, y, '-', linewidth = 2, label = '$x**$' + str(i+1)) # Plotando gráfico x**i    
        ax.legend(loc = 'lower right') # Localização dos rótulos das funções
        ax.set_xticks([-1, 0, 1]) # Números no eixo x
        ax.set_yticks([-1, 0, 1]) # Números no eixo y
    plt.show()
    return None

def fun(a, b, n):
    fig, ax = plt.subplots(figsize = (6, 6)) # Quadro de tamanho 6x6 e frame
    x = np.linspace(a, b, n, dtype = float) # n pontos no intervalo [a, b]
    des = np.where(abs(np.diff(np.sign(np.sin(x)))) > 1)[0]+ 1 # Procuro os índices de intervalo entre um positivo e um negativo
    x = np.insert(x, des, np.nan) # Coloco np.nan nos intervalos das descontinuidades
    pos = np.where(np.sin(x) == 0) # Procuro onde seno é zero
    y = 1/(np.sin(x)) # Defino y
    y[pos] = np.nan # Descarto os pontos onde seno é nulo substituindo por np.nan
    inf = np.where(abs(y) > 20)[0] # Procuro os índices onde módulo de y é maior que 20
    x = np.delete(x, inf) # Deleto os valores de x que resulta y > 20
    y = np.delete(y, inf) # Deleto os valores de y > 20
    ax.plot(x, y, 'c-o', label = '$y = 1/sin(x)$') # Escrevo o rótulo
    ax.legend(loc = 'upper center') # Localizo o rótulo
    plt.show()
    return des
