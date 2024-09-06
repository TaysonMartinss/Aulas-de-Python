class Restaurante:
    Nome = ''
    Categoria = ''
    Ativo = bool


estabelecimento1 = Restaurante()
estabelecimento1.Nome = 'PizzaRiba'
estabelecimento1.Categoria = 'Italiana'
estabelecimento1.Ativo = False

print(f'Restaurante:{estabelecimento1.Nome} | Categoria: {estabelecimento1.Categoria} | Status {estabelecimento1.Ativo}')
print(vars(Restaurante))
