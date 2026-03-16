info1 = {
    'nome': 'Notebook',
    'preco': 3500.00
}

info2 = {
    'marca': 'TechBrand',
    'estoque': 15
}

info3 = {**info1, **info2}
info3['preco'] = 3200.00
print(info3)