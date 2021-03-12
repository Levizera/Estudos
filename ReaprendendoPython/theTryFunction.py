#Funcão quebrada pra testar o TRY e EXCEPT
def somandoString():
    palavra = "Olá Mundo"
    numero = 2
    print(palavra + numero)

try :
    somandoString()
except : 
    mensagemDeErro = "Código quebrou"

print(mensagemDeErro)

#O statement try serve para testar um codigo, se caso ele estiver quebrado, ele mesmo assim irá testar o codigo. Dentro do TRY você pode colocar o EXCEPT para que ele mostre uma mensagem dizendo se o seu código está quebrado ou não. 
