# Hoje dia 17/08/22 estou começando a codar pela primeira vez#

# Como concantenar strings , primeiro colocar dentro de uma variavel um valor e depois não esquecer de colocar um espaço antes da ultima aspa para ter espaço entre cada string quando for printar. 

nome1 = "Antonio"

print(nome1)

nome2 = " Bezerra"

print(nome1 + nome2)

nome3 = " da"

nome4 = " Silva"

print(nome1 + nome2 + nome3 + nome4)
print(nome1 + nome2 + nome3 + nome4 + " idade: 52 anos")

print("iniciando nas funções de Python")

# estudo de difereça entre listas , tuplas e dicionario
# primeiro vamos ver listas ,as listas são usadas as seguintes estruturas nome da lista depois o sinal de igual e os elementos da lista devem estar entre colchetes e divididos por virgulas

computador = ["teclado", "mouse", "monitor", "desktop"]
print(computador)

# em uma lista podemos ter varios elementos diferentes como: strings, inteiros, float e boleanos

lista1 = ['casa', 5, 4.2, True, False]
print(lista1)

#para saber o tipo dessa variavel utiliza-se a seguinte estrutura print mais  abrir parenteses ,mais type, abrir parenteses,colocar o nome da variavel, fechar parentes e fecharparenteses

print(type(lista1))

# para obter um elemento especifico da lista nos usamos o indice a que cada elemento tem começando a partir do primeiro indice que é o zero.

print(lista1[4])

# para acrescentar algum item na minha lista eu posso usar o .append da seguinte forma coloca-se a variável no nosso caso list1 ponto append abre parênteses coloca o valor e fecha o parênteses

lista1.append('cavalo')

print(lista1)

# nesse caso ele entra depois dos outros itens itens já existentes na lista

# para inserir novos itens na lista em uma posição determinada usamos o .insert da seguinte maneira: o nome da lista mais o .insert e entre parenteses o índice e o item a ser inserido e fecha o parênteses

lista1.insert(2, 'chocolate ')

print(lista1)

# para remover um item na lista nos temos vários comandos,  o primeiro é .remove,  o segundo é .pop e o terceiro é del,  usamos da seguinte maneira:  o nome da lista mais o .remove e entre parenteses o nome do item a ser removido.

lista1.remove('cavalo')

print(lista1)

# usamos .pop da seguinte forma coloca-se o nome mais .pop e entre parenteses coloca-se o índice de acordo com o item a ser eliminado.

lista1.pop(0)

print(lista1)

# Para usar o del primeiro colocamos del espaço  o nome da lista e entre colchetes o índice do item a ser excluído.

del lista1[2]

print(lista1)

# se você colocar o .pop entre parenteses vazio ele ira eliminar o ultimo elemento da lista, a diferença entre .pop e del é que quando você usa o .pop você consegue recuperar o elemento retirado enquanto que com o del não é possivel.

lista1.pop()

print(lista1)

# Nas listas nos podemos fatiar ou fazer slices usando varios parametros atraves do indice para mostrar determinados elementos da lista.

lista2 = [51, 10, 8, 4, 19, 32, 24, 11, 5, 2, 25, 7]

# usamos o sort() para ordenar uma lista de maneira crescente do menor para o maior 

lista2.sort()

print(lista2)

# Usamos o len para saber quantos elementos temos dentro da lista. 

print(len(lista2))

# Nesse caso fatiamos na lista do indice 0 até o indice 3. 

print(lista2[0:4])

# Nesse caso ocorreu a repetição da sequencia anterior porque quando não selecionamos o parametro inicial o python entende que estamos iniciando do indice 0 .

print(lista2[:4])

# nesse caso como só aparece apenas o primeiro parametro o python entende que começa do indice 0 e vai até o ultimo indice.

print(lista2[0:])

# podemos usar tambem o indice negativo para buscar do final da lista para o inicio. 

print(lista2[-1])

# para saber o tipo de dados de minha lista eu uso o comando type() . 

print(type(lista2))












