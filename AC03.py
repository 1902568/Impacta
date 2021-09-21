class Calculadora:
    def __init__(self, numero1, numero2, operador):
        self.numero1 = numero1
        self.numero2 = numero2
        self.operador = operador

    def sum(self):
        return self.numero1 + self.numero2

    def subtraction(self):
        return self.numero1 - self.numero2

    def multiplication(self):
        return self.numero1 * self.numero2

    def division(self):
        return self.numero1 / self.numero2


class Operacao(Calculadora):
    def __init__(self, numero1, numero2, operador):
        self.numero1 = numero1
        self.numero2 = numero2
        self.operador = operador

    def calculate(self):
        if self.operador == "+":
            return(operacao.sum(self))
        elif self.operador == "-":
            return(operacao.subtraction(self))
        elif self.operador == "*":
            return(operacao.multiplication(self))
        elif self.operador == "/":
            return(operacao.division(self))


sum = operacao(10, 5, "+")
sub = operacao(10, 5, "-")
multi = operacao(10, 5, "*")
div1 = operacao(10, 5, "/")
print(sum.calculate())
print(sub.calculate())
print(div.calculate())
print(div.calculate())
