contato = {
    'nome': 'Victor',
    'telefone': '4002-8922',
    'email': 'victorhugomdarocha@gmail.com',
    'cidade': 'Piraubinha'
}
chave_email = False

contato['Instagram'] = 'victorrochx' # b
del contato['telefone']

for chave, valor in contato.items():
    print(f'{chave} -> {valor}') # a
    if chave == 'email':
        chave_email = True

if chave_email == True:
    print('A chave email está cadastrada')
else:
    print('A chave email não está cadastrada')