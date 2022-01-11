class Cliente:
    def __init__(self, nome, email, idade, cpf, plano):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.cpf = cpf
        planos = ['Basic', 'Gold', 'Premium']
        if plano in planos:
            self.plano = plano
        else:
            raise Exception('Opa! Plano inválido.')


lista = ['Basic', 'Gold', 'Premium']
opcoes = int(input('Escolha: 0 = Basic / 1 = Gold / 2 = Premium: '))
if opcoes > 2:
    raise Exception('Opa! Plano inválido!')
else:
    r = lista[opcoes]


cliente = Cliente('Samuel', 'samuel@trigueiros.com', 23, '07803306500', r)
print(cliente.email)
print(cliente.nome)
print(cliente.plano)
