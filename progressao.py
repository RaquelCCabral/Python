class Sequencia:
    def __init__(self, seq):
        self.s = seq

    def classificacao(self):
        for i in range(len(self.s)-1):
            if self.s[i+1]>self.s[i]:
                return 'crescente'
            elif self.s[i+1]< self.s[i]:
                return 'decrescente'
            else:
                return 'constante'

    def progressao(self):
        r0, q0 = [self.s[1] - self.s[0]], [self.s[1]/self.s[0]]
        for i in range(len(self.s)-1):
            r, q = self.s[i+1] - self.s[i], self.s[i+1]/self.s[i]
            r0.append(r)
            q0.append(q)
        if len(set(r0)) == 1:
            return 'PA'
        elif len(set(q0)) == 1:
            return 'PG'
        else:
            return 'Não é PA nem PG'

    def razao(self):
        if self.progressao() == 'PA':
            r = self.s[1] - self.s[0]
        elif self.progressao() == 'PG':
            r = self.s[1]/self.s[0]
        return r

    def enesimo_termo(self, n):
        if self.progressao() == 'PA':
            an = self.s[0] + (n-1)*self.razao()
        elif self.progressao() == 'PG':
            an = self.s[0]*self.razao()**(n-1)
        return an

    def soma_dos_termos(self, n):
        if self.progressao() == 'PA':
            sn = (self.s[0] + self.enesimo_termo(n))*n/2
        elif self.progressao() == 'PG':
            sn = (self.s[0]*(self.razao()**(n) - 1))/(self.razao() - 1)
        return sn

    def soma_inf_dec(self):
        if self.progressao() == 'PG' and self.classificacao() == 'decrescente':
            return self.s[0]/(1 - self.razao())