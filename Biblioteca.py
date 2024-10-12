class Pessoa:

    def __init__(self, nome, idade, peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.acao = None
    def falar(self):
        if self.acao is None:
            self.acao = 'falando'
            print(f'{self.nome} está falando.')
        else:
            print(f'{self.nome} já está {self.acao}. Ele não pode fazer outra coisa agora.')

    def comer(self):
        if self.acao is None:
            self.acao = 'comendo'
            print(f'{self.nome} está comendo.')
        else:
            print(f'{self.nome} já está {self.acao}. Ele não pode fazer outra coisa agora.')

    def dormir(self):
        if self.acao is None:
            self.acao = 'dormindo'
            print(f'{self.nome} está dormindo.')
        else:
            print(f'{self.nome} já está {self.acao}.Ele não pode fazer outra coisa agora.')

    def andar(self):
        if self.acao is None:
            self.acao = 'andando'
            print(f'{self.nome} está andando.')
        else:
            print(f'{self.nome} já está {self.acao}. Ele não pode fazer outra coisa agora.')

    def fim(self):
        if self.acao is not None:
            infinitivo = {
                'comendo': 'comer',
                'andando': 'andar',
                'dormindo': 'dormir',
                'falando': 'falar'
            }
            print(f'{self.nome} terminou de {infinitivo[self.acao]}.')
            self.acao = None
        else:
            print(f'{self.nome} não está fazendo nada no momento.')

