
""""
Herança é um conceito do paradigma da orientação à objetos que determina que uma classe (filha)
pode herdar atributos e métodos de uma outra classe (pai) e, assim, evitar que haja muita repetição de código.
"""

class Produto:
    def __init__(self, produto, preco, custo):
        self.nome = str(produto)
        self.preco = preco
        self.custo = custo

    def exibir(self):
        print(f'PRODUTO..............{self.nome}')
        print(f'PREÇO DO ANÚNCIO.....R${self.preco}')
        print(f'PREÇO DE CUSTO.......R${self.custo}')

class Calculadora(Produto):   #HERDANDO  ATRIBUTOS E MÉTODOS DA CLASSE PRODUTO
    def __init__(self, produto, preco, custo):
        Produto.__init__(self, produto, preco, custo)  #Acessando método INIT da classe pai
        self.taxa = 0
        self.frete = 20

    def premium(self):
        self.taxa = self.preco * 18 / 100
        print('ANÚNCIO PREMIUM:')
        super().exibir()  #Acessando método da classe Pai
        print(f'TAXA ML..............R${self.taxa}')
        print(f'FRETE................R${self.frete}')
        print(f'LUCRO................R${self.preco - self.custo - self.taxa - self.frete}')
        print('________________')

    def clasico(self):
        self.taxa = self.preco * 13 / 100
        print('ANÚNCIO CLÁSSICO:')
        super().exibir()  #Acessando método da classe pai
        print(f'TAXA ML..............R${self.taxa}')
        print(f'FRETE................R${self.frete}')
        print(f'LUCRO................R${self.preco - self.custo - self.taxa - self.frete}')
        print('________________')

#
# p1 = Calculadora('Fone', 279, 90)
# p1.premium()
# p1.clasico()

# p2 = Calculadora('Amplificador', 389, 180)
# p2.premium()
# p2.clasico()
#
# p3 = Calculadora('Lipocavitação', 1079, 400)
# p3.premium()
# p3.clasico()



