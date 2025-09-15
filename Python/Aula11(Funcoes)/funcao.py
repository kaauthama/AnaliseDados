# O codigo abaixo sma e imprime no terminal a soma de 2 + 2
# print(2+2)


#-=-=-=-=-=-=-=-=-=-=-=-=-=-Funções-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Abaixo temos uma funcao que realiza a soma de 2 numeros
def somaDakau(a, b): #soma com 2 numeros
    return(a + b)

# Função que divide dois números
def divideDakau(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a / b
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


#-=-=-=-=-=-=-=-=-=-=-=-=-=-Chamada de Funções-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
somaDeDoisNumeros = somaDakau(2, 2)

print(divideDakau(somaDeDoisNumeros, 2)) #chamada da funcao soma com 2 numeros e imprime o resultado no terminal