largura_da_parede = float(input('Qual a largura da sua parede? '))
altura_da_parede = float(input('Qual a altura da sua Parede? '))
dimensao_da_parede = largura_da_parede * altura_da_parede
litros_de_tinta = dimensao_da_parede / 2

print(f'Sua parede tem a dimensão de {largura_da_parede} x {altura_da_parede} e sua dimensão é de {dimensao_da_parede}m2. Para pintar essa parede você vai precisar de {litros_de_tinta}L de tinta ')
