import hashlib

def inserindo_dados():
    usuario = input('Insira o seu usuario: ')
    email = input('Insira o seu email: ')
    senha = input('Insira a sua senha: ')
    url = input('Insira a URL do site: ')
    hashed_usuario = hashlib.sha256(usuario.encode('utf-8')).hexdigest()
    hashed_email = hashlib.sha256(email.encode('utf-8')).hexdigest()
    hashed_senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()

    print(f''' 
Seus dados ↓

Usuario : {hashed_usuario} 

Email : {hashed_email}

Senha : {hashed_senha}

Senha {url}

''')

inserindo_dados()