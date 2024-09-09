from modelos.avaliacao import Avalicao
#isso é uma classe (um conjunto de atributos e metodos que seus objetos ou instancias terão)
class Restaurante:
    restaurantes = []
    #init é o construtor, ele inia os atributos da instancia que eu escolhi no caso nome e categoria
    #quando chamo ele dentro de ua classe eu estou definindo como as coisas vão ocorrer

    def __init__(self, nome, categoria):
        #self é uma maneira de permitir que cada objeto se refira a si mesmo
        self._nome = nome.title() #.title coloca o parametro em letra maiuscula
        self._categoria = categoria.upper() # .upper coloca todas as letras maiusculas
        self._ativo = False  # colocar _antes do nome do ativo diz para o construtor que a gente não espera que esse parametro seja instanciado
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria} '
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
       
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} |{str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo} ')


    @property
    def ativo(self):
     return '✓' if self._ativo else '✕'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avalicao = Avalicao(cliente, nota)
        self._avaliacao.append(avalicao)
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas,1)
        return media


# estou usando os métodos do objeto ( no caso estou usando a função 
# que esta dentro da classe Restaurantes que server para listar restaurantes cadastrados que foram adicionados 
# na lista no momento da iniciação (__init__) em uma lista que tabem esta dentro da classe Restaurante  )

Restaurante.listar_restaurantes()

# Instância:  O ato de criar um objeto a partir de uma classe

# Objeto: A entidade concreta criada pela instância, que possui dados e métodos associados.


#########################################################################
# Métodos de Instância:
# Definição: São métodos que operam em instâncias individuais da classe. Eles têm acesso aos atributos e métodos da instância específica e usam o self como o primeiro parâmetro.

# Uso: São usados para acessar ou modificar o estado específico de uma instância.


# Métodos de Classe:
# Definição: São métodos que operam na classe como um todo, em vez de em instâncias individuais. Eles têm acesso aos atributos e        métodos da classe e usam o cls como o primeiro parâmetro.

# Uso: São usados para criar ou modificar o estado que é compartilhado entre todas as instâncias da classe. São úteis para criar métodos de fábrica, acessar ou modificar atributos de classe.

# Quando Usar Cada Tipo de Método:
# Métodos de Instância: Use quando precisar operar sobre dados específicos da instância, como atributos e comportamentos que variam entre diferentes instâncias.

# Métodos de Classe: Use quando precisar de uma operação que afeta a classe como um todo ou quando precisar de um método que não depende do estado de uma instância específica, como métodos de fábrica para criar novas instâncias de maneira controlada.

###########################################################################################################################

# @property é ideal quando você quer criar atributos que dependem de cálculos ou transformações a partir de outros atributos da instância.

# @classmethod é útil para operações que estão relacionadas à classe como um todo, como criar instâncias de maneiras especiais ou manter estado compartilhado entre todas as instâncias da classe.





###########################################################################