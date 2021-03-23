# Utilizando o codigo "abstracao_de_dados.py" como modulo

from abstracao_de_dados import Fila

supermercado = Fila()
loterica = Fila()
banco = Fila()

supermercado.entrar_na_fila('Levi')

print(supermercado.fila)
