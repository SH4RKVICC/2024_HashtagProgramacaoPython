# 1. Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 números como parâmetro e retornar a soma deles.

# Recebendo valores;
n1 = float(input("Insira o primeiro número desejado: "))
n2 = float(input("Insira o segundo número desejado: "))

# Desenvolvendo Função;
soma = lambda x, y: x + y
resultado = list(map(lambda x: f"Resultado: {x}", [soma(n1, n2)]))

# Mostrando resultado;
print(resultado)