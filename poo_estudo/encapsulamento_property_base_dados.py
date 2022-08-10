""""
Encapsulamento é um dos pilares da programação orientada a objetos.
É a proteção dos atributos ou métodos de uma classe

Public, Protected, Private
_ Protected (consigo acessar -> _NOMEATRIBUTO)
__ Private (consigo acessar -> _NOMECLASSE__NOMEATRIBUTO)
____________________________________________________________

Property é usada para dar uma funcionalidade "especial" a certos métodos para fazer com que ajam
como getters, setters ou deleters quando definimos as propriedades em uma classe.

Um getter - para acessar o valor do atributo.
Um setter - para definir o valor do atributo.
Um deleter - para excluir o atributo de instância.
"""

class BancoDados:

    def __init__(self):
        self.__bd = [] #Atributo privado/encapsulado

    def adiocionar_usuario(self, nome: str, cpf: str) -> None:
         self.bd = ([nome, cpf])

    #Getter
    @property #Obtendo/acessando atributo privado
    def bd(self):
        return self.__bd #Retornado valor do atributo privado

    #Setter
    @bd.setter #Configurando/tratando e definindo novos valores ao atributo
    def bd(self, novo_valor):
        if novo_valor not in self.__bd:
            if isinstance(novo_valor, list):
                var = novo_valor[1].replace('.', '')
                if len(var) == 11:
                    self.__bd.append(novo_valor)
                    print('Adicionado novo valor')

                else:
                    print('Numero de CPF inválido')

        else:
            print("Usuário já cadastrado!")


# base = BancoDados()
# base.adiocionar_usuario('Pedro', '46305131830')
# base.adiocionar_usuario('Paulo', '463.081.320.30')
# base.adiocionar_usuario('Roberto', '544455')
# base.adiocionar_usuario('Bruna', '544455')
# base.adiocionar_usuario('Pedro', '46305131830')
# base.adiocionar_usuario('Paulo', '463.081.320.30')

#Acessando atribudo pelo Poperty
# print(base.bd)