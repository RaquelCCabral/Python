dec = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rom = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

def romanos(n):
    if type(n) == int and 0 < n < 4000:
        lista = []
        i = 0
        while i <= 12:
            div = n//dec[i]
            n %= dec[i]
            while div:
                lista.append(rom[i])
                div -= 1
            i += 1
        numero_romano = ''.join(lista)
        return numero_romano
    else:
        print('Insira um número entre 0 e 4000.')

conversor = dict(zip(rom, dec))

def decimais(string):
    if type(string) == str:
        string = string.upper()
        num = 0
        for i in range(len(string)):
            try:
                x = conversor[string[i]]
                if i + 1 < len(string) and conversor[string[i + 1]] > x:
                    num -= x
                else:
                    num += x
            except KeyError:
                num = 'Verifique as letras digitadas.'
    return num