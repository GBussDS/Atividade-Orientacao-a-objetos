class Produto:

    #Atributo estatico
    codigo_barras_atual = 0

    def __init__(self, categoria, preco, marca):
        self.categoria = categoria
        Produto.codigo_barras_atual = Produto.codigo_barras_atual + 1
        self.codigo_de_barras = Produto.codigo_barras_atual
        self.preco = preco
        self.marca = marca
        self.nome_estoque = ""
    
    #Retorna o código de barras
    def get_codigo_de_barras(self):
        return self.codigo_de_barras

    #Retorna o preço
    def get_preco(self):
        return self.preco
    
    #Retorna a categoria
    def get_categoria(self):
        return self.categoria

    #Retorna a marca
    def get_marca(self):
        return self.marca
    
    def get_nome_estoque(self):
        return self.nome_estoque

    #Define como o produto vai ser printado
    def __str__(self):
        return f"Produto do tipo: {self.categoria}. Código de barras: {self.codigo_de_barras}\n"

class Roupa(Produto):

    def __init__(self, preco, marca, tipo, cor):
        super().__init__("Roupa", preco, marca)
        self.tipo = tipo
        self.cor = cor
        self.nome_estoque = f"{self.tipo} {self.cor}"

    def vestir(self):
        print(f"Você está vestindo {self.tipo} da cor {self.cor} da marca {self.marca}.\n")

    #Retorna o tipo de roupa
    def get_tipo(self):
        return self.tipo
    
    #Retorna a cor da roupa
    def get_cor(self):
        return self.cor

class Manga(Produto):

    def __init__(self, preco, marca, titulo, autor, bTraduzido):
        super().__init__("Manga", preco, marca)
        self.titulo = titulo
        self.autor = autor
        self.bTraduzido = bTraduzido
        if self.bTraduzido:
            self.nome_estoque = f"{self.titulo} traduzido"
        else:
            self.nome_estoque = f"{self.titulo}"

    def ler(self):
        if self.bTraduzido == "sim" or self.bTraduzido:
            print(f"Você está lendo {self.titulo}, escrito por {self.autor}.\n")
        else:
            print(f"Você está lendo {self.titulo}, escrito por {self.autor}.")
            print("Como você sabe japonês?\n")
    
    def get_titulo(self):
        if self.bTraduzido:
            return f"{self.titulo} traduzido"
        else:
            return f"{self.titulo}"

class Jogo(Produto):
    
    def __init__(self, preco, marca, nome, console):
        super().__init__("Jogo", preco, marca)
        self.nome = nome
        self.console = console
        self.nome_estoque = f"{self.nome} {self.console}"

    def jogar(self):
        print(f"Você está jogando {self.nome} em um {self.console}.\n")

    #Retorna o nome do jogo
    def get_nome(self):
        return self.nome

    #Retorna o console do jogo
    def get_console(self):
        return self.console
