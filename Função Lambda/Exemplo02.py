# Aplicando Função dentro de outros Métodos do Python;

precos = [100, 500, 10, 25] # Criando Lista de Preços;

impostos = list(map(lambda x: x *0.3, precos)) # Criando variavel imposto e aplicando lambda;

print(impostos) # Mostrando Resultado;