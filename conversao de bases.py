def conversao(n, x, y):

    letra_numero = {'A':'10', 'B':'11', 'C':'12', 'D':'13', 'E':'14', 'F':'15'}
    numero_letra = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}

    def numero_valido(n):
        try:
            if abs(int(float(n))) == int(n):
                return True
            else:
                return False
        except ValueError:
            if n[0] == '-':
                return False
            else:
                return True

    if numero_valido(n):
        if 10 < x <= 16:
            l = []
            for i in range(len(n)):
                l.append(n[i])
                if n[i] in letra_numero.keys():
                    l[i] = letra_numero[n[i]]
            l.reverse()
            d = 0
            for i in range(len(l)):
                d += int(l[i]) * x**i
        elif 2 <= x <= 10:
            a = [int(i) for i in str(n)]
            a.reverse()
            j, d = 0, 0
            while j < len(a):
                d = d + a[j] * x**j
                j+= 1
        else:
            return 'Apenas bases de 2 a 16'

        if y == 10:
            return d
        else:
            q = d
            l = []
            r = 0
            while q > 0:
                r = q % y
                l.append(r)
                q = q//y
            l.reverse()
            s = [str(k) for k in l]
            if 10 < y <= 16:
                for i in range(len(l)):
                    if l[i]>= 10:
                        try:
                            s[i] = numero_letra[s[i]]
                        except KeyError:
                            continue
            num = ''.join(s)
        return num
    else:
        return 'Apenas inteiro positivos!'