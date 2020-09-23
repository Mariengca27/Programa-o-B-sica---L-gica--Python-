# ler um número inteiro e outro real e imprimir ambos  na tela, e a soma dos dois também.   
 
a = int(input(" Digite um número inteiro"))
b = int(input(" Digite um número real"))
# Lembrar e colocar o tipo de dado que está sendo inserido.

som = a + b
print(a)
print(type(som))
print(som)
print(b)


#Transformar isso em uma calculadora básica para o usuário ver a operação que está sendo feita. Começar fazendo pela soma 

print('{} + {} ='.format(a,b))
print(a + b)

#Agora fazer com os restantes:

print('{} + {} ='.format(a,b))
print(a - b) 
print("Esse é o resultado da conta de sub.")

print('{} + {} ='.format(a,b))
print(a * b)
print("Esse é o resultado da conta de multi")

print('{} + {} ='.format(a,b))
print(a / b)
print("Esse é o resultado da conta de div.")