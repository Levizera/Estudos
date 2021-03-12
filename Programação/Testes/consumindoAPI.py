import requests

def consultaDeCEP():
   print('''
==============
Consulta CEP 
==============

''')

   cepInput = input('Digite seu CEP: ')
   
   if len(cepInput) != 8:
      print('Quantidade de Digitos do CEP Inválidos, Tente Novamente!!!')
      exit()
      
   request = requests.get(f'https://viacep.com.br/ws/{cepInput}/json/')
   request_adress = request.json()
   
   if 'erro' not in request_adress :
      print(f'''
      ==> CEP Encontrado com Sucesso! <==
      
      Informações: 
      
      CEP: {request_adress["cep"]}
      Localidade: {request_adress["localidade"]}
      UF: {request_adress["uf"]}   
      Logradouro: {request_adress["logradouro"]}
      Bairro: {request_adress["bairro"]}
      ''')
   else : 
      print(f'{cepInput} : CEP Inválido, Tente Novamente!!!')
      
   maisConsultas = int(input('''
   
   Deseja consultar mais um CEP??
   
   [1] Sim!
   [2] Não!
   
   --> '''))
   
   if maisConsultas == 1:
      return consultaDeCEP()
   else:
      print('Okay, Muito Obrigado por usar os nossos serviços :)')
      exit()
      
      
consultaDeCEP()