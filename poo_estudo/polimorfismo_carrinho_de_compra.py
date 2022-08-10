""""
Polimorfismo, em Python, é a capacidade que uma subclasse tem de ter métodos com o  mesmo
nome de sua superclasse, e o programa saber qual método deve ser invocado, especificamente
(da super ou sub). Ou seja, o objeto tem a capacidade de assumir diferentes formas (polimorfismo).
"""

from poo_estudo.heranca_calculadora_ml import Produto

class ComprarMl(Produto): #Herdando atributos e métodos da classe Produto.
    def __init__(self, produto, preco, custo):
        super().__init__(produto, preco, custo)

    def adiocionar_produto(self) -> None:
        print(f'Adicionado {self.nome} no carrinho do MERCADO LIVRE.')

    def comprar_produto(self) -> None:
        print(f'Comprado {self.nome} efetuada com sucesso no MERCADO LIVRE.')

class ComprarShopee(Produto): #Herdando atributos e métodos da classe Produto.
    def __init__(self, produto, preco, custo):
        super().__init__(produto, preco, custo)

    # Método com o mesmo nome da classe "ComprarML", porém com outrO formato (POLIMORFISMO).
    def adionando_produto(self) -> None:
        print(f'Adicionado {self.nome} no carrinho da SHOPEE.')

    # Método com o mesmo nome da classe "ComprarML", porém com outrO formato (POLIMORFISMO).
    def comprar_produto(self) -> None:
        print(f'Comprado {self.nome} efetuada com sucesso NA SHOPEE.')


# produto1 = Produto('Fone', 279, 90)
# p1 = ComprarShopee
# p1.adionando_produto(produto1)
# p1.comprar_produto(produto1)
#
# print('------------------------------------')
#
# produto2 = Produto('Amplificador', 380, 190)
# p2 = ComprarMl
# p2.adionando_produto(produto2)
# p2.comprar_produto(produto2)