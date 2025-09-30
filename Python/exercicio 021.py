# strip() remove espaços extras no início e no fim.

# upper() padroniza a frase em maiúsculas para facilitar a contagem.

# count('A') conta quantas vezes "A" aparece.

# find('A') retorna a posição da primeira ocorrência (começa do 0, por isso somamos 1).

# rfind('A') retorna a posição da última ocorrência (também somamos 1).
frase = input('Digite uma frase: ').strip().upper()

quantidade = frase.count('A')
primeira_posicao = frase.find('A') + 1
ultima_posicao = frase.rfind('A') + 1

print('A letra A aparece {} vezes na frase.'.format(quantidade))
print('A primeira letra A apareceu na posição {}.'.format(primeira_posicao))
print('A última letra A apareceu na posição {}.'.format(ultima_posicao))

