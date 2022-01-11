class ControleRemoto:
    def __init__(self, preco, cor, altura, largura, profundidade):
        # aqui vão os atributos da classe
        self.preco = preco
        self.cor = cor
        self.altura = altura
        self.largura = largura
        self.profundidade = profundidade

    def passar_de_canal(self, tecla):

        if tecla == '+':
            print("Subir um canal")
        elif tecla == '-':
            print("Descer um canal.")
        else:
            print("Tecla inválida.")


controle_remoto = ControleRemoto(79.56, 'cinza', 15.6, 5.7, 2.5)
print(controle_remoto.cor)
botao = input('Aumentar canal (+) / Diminution canal (-): ')
controle_remoto.passar_de_canal(botao)
