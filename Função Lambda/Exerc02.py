#2. Faça um programa que solicite dois números ao usuário e exiba a multiplicação deles. A multiplicação deve ser calculada em uma função lambda.

# Recebendo valores;
n1 = float(input("Insira o primeiro número desejado: "))
n2 = float(input("Insira o segundo número desejado: "))

# Desenvolvendo Função;
mult = lambda x, y: x * y
resultado = list(map(lambda x: f"Resultado: {x}", [mult(n1, n2)]))

# Mostrando resultado;
print(resultado)