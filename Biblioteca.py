class Pessoa:

    def __init__(self, nome, idade, peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.andando = False
        self.falando = False
        self.comendo = False
        self.dormindo = False

    def falar(self):
        self.falando = True

        print(f'{self.nome} foi falar.')
        if self.falando == True and self.dormindo == False and ea

    def pararfalar(self):
        print(f'{self.nome} parou de falar.')
    def comer(self):
        print(f'{self.nome} foi comer.')
        self.comendo = True
    def dormir(self):
        print(f'{self.nome} foi dormir.')
        self.dormindo = True
    def andar(self):
        print(f'{self.nome} foi andar')
        self.andando = True

