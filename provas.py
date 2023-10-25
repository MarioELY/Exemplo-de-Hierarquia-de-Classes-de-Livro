# Definindo a classe base "Livro"
class Livro:
    def __init__(self, titulo, autor, editora):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Editora: {self.editora}")

# Definindo a classe "Romance" que herda de "Livro"
class Romance(Livro):
    def __init__(self, titulo, autor, editora, numero_paginas, faixa_etaria):
        super().__init__(titulo, autor, editora)  # Chama o construtor da classe base
        self.numero_paginas = numero_paginas
        self.faixa_etaria = faixa_etaria

    def exibir_detalhes(self):
        super().exibir_detalhes()  # Chama o método da classe base para exibir informações comuns
        print(f"Número de Páginas: {self.numero_paginas}")
        print(f"Faixa Etária Recomendada: {self.faixa_etaria}")

# Definindo a classe "Biografia" que herda de "Livro"
class Biografia(Livro):
    def __init__(self, titulo, autor, editora, pessoa_biografada, data_publicacao):
        super().__init__(titulo, autor, editora)  # Chama o construtor da classe base
        self.pessoa_biografada = pessoa_biografada
        self.data_publicacao = data_publicacao

    def exibir_detalhes(self):
        super().exibir_detalhes()  # Chama o método da classe base para exibir informações comuns
        print(f"Pessoa Biografada: {self.pessoa_biografada}")
        print(f"Data de Publicação: {self.data_publicacao}")

# Solicita ao usuário informações sobre o livro de Romance.
titulo_romance = input("Digite o título do romance: ")
autor_romance = input("Digite o autor do romance: ")
editora_romance = input("Digite a editora do romance: ")
num_paginas_romance = input("Digite o número de páginas do romance: ")
faixa_etaria_romance = input("Digite a faixa etária recomendada do romance: ")

# Solicita ao usuário informações sobre o livro de Biografia.
titulo_biografia = input("Digite o título da biografia: ")
autor_biografia = input("Digite o autor da biografia: ")
editora_biografia = input("Digite a editora da biografia: ")
pessoa_biografada = input("Digite a pessoa biografada na biografia: ")
data_publicacao = input("Digite a data de publicação da biografia: ")

# Cria instâncias dos livros com os dados fornecidos pelo usuário
livro_romance = Romance(titulo_romance, autor_romance, editora_romance, num_paginas_romance, faixa_etaria_romance)
livro_biografia = Biografia(titulo_biografia, autor_biografia, editora_biografia, pessoa_biografada, data_publicacao)

# Imprime os detalhes do romance
print("\nDetalhes do Romance:")
livro_romance.exibir_detalhes()

# Imprime os detalhes da biografia
print("\nDetalhes da Biografia:")
livro_biografia.exibir_detalhes()
