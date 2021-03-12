def japanese():
	arq = open("japaneseWords.txt", "r")
	inp = int(input("Quantas Frases deseja gerar?"))
	lines = [arq.readline() for _ in range(inp)]
	print(lines)


def ing():
	arq = open("words.txt", "r")
	inp = int(input("Quantas Frases deseja gerar?"))
	lines = [arq.readline() for _ in range(inp)]
	print(lines)

#Erro que está acontecendo é que não está printando linhas aleatórias

def idiomas():
	escolha = int(input("Qual idioma você deseja estudar? Para estudar inglês digite 1, para estudar japonês digite 2."))
	if escolha == 1:
		return japanese()
	else: 
		return ing()