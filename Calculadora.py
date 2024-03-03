# Importando a biblioteca math para operações matemáticas
import math

# Definindo classe e funções
class calculadora:
    def adicao(self, x, y):
        return x + y
    
    def subtracao(self, x, y):
        return x - y
    
    def multiplicacao(self, x, y):
        return x*y
    
    def divisao(self, x, y):
        if y != 0:
            return x*y
        else:
            return "Erro! Divisão por zero!"
        
    def raiz_quadrada(self, x):
        return math.sqrt(x)
    
    def raiz(self, x, y):
        return x**(1/y)
    
    def potencia(self, x, y):
        return x**y
    
    def porcentagem(self, x, y):
        return x * (y / 100)
    
# Instância para a classe Calculadora
calculadora = Calculadora()

# Dicionário de símbolos das operações
operacoes = {
    '+': calculadora.adicao,
    '-': calculadora.subtracao,
    '*': calculadora.multiplicacao,
    '/': calculadora.divisao,
    'raiz2': calculadora.raiz_quadrada,
    'raiz': calculadora.raiz,
    'pot': calculadora.potencia,
    '%': calculadora.porcentagem
}

while True:
    # Recebendo o input do usuário
    num1 = float(input("Insira o primeiro número: "))

    #  Menu de operações
    print("Selecione a operação:")
    for simbolo in operacoes.keys():
        print(f"{simbolo} : {operacoes[simbolo].__name__}")

    operador = input("Insira o símbolo para a operação: ")

    # Realizando o cálculo com base no operador escolhido
    if operador in operacoes:
        if operador in ('+', '-', '*', '/', 'raiz', 'pot'):
            num2 = float(input("Insira o segundo número: "))
            resultado = operacoes[operador](num1, num2)

        elif operador == 'raiz2':
            resultado = operacoes[operador](num1)

        elif operador == '%':
            y = float(input("Insira a porcentagem desejada: "))
            resultado = operacoes[operador](num1, y)

    else:
        resultado = "Símbolo inválido!"

    # Exibindo o resultado
    print(f'Resultado: {resultado}')

    # Perguntar ao usuário se ele deseja outro cálculo
    outro_calculo = input("Você deseja realizar outra operação? (sim/não): ")
    if outro_calculo.lower() != 'sim':
        break
