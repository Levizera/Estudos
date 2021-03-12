from translate import Translator
from time import sleep 

idiomas = Translator(from_lang="english", to_lang="Portuguese")

resposta = idiomas.translate(input("Entre com a palavra para traduzir do inglês para português: "))

print("Processando...")
sleep(2)
print(resposta.upper())