class Pessoa:

    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.acao = None
    def falar(self):
        if self.acao is None:
            self.acao = 'falando'
            print(f'{self.nome} está falando.')
        else:
            print(f'{self.nome} já está {self.acao}. Não pode fazer outra coisa agora.')

    def comer(self):
        if self.acao is None:
            self.acao = 'comendo'
            print(f'{self.nome} está comendo.')
        else:
            print(f'{self.nome} já está {self.acao}. Não pode fazer outra coisa agora.')

    def dormir(self):
        if self.acao is None:
            self.acao = 'dormindo'
            print(f'{self.nome} está dormindo.')
        else:
            print(f'{self.nome} já está {self.acao}. Não pode fazer outra coisa agora.')

    def andar(self):
        if self.acao is None:
            self.acao = 'andando'
            print(f'{self.nome} está andando.')
        else:
            print(f'{self.nome} já está {self.acao}. Não pode fazer outra coisa agora.')

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

class Animal:
    def __init__(self, nome, cor):
        self.cor = cor
        self.nome = nome
    def comer(self):
        print(f'{self.nome} foi comer.')
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def miar(self):
        print(f'{self.nome} está miando.')
class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def latir(self):
        print(f'{self.nome} está latindo.')
class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def mujir(self):
        print(f'{self.nome} está mujindo.')
class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def chiar(self):
        print(f'{self.nome} está chiando.')

class Atleta:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.aposentado = False
        self.aquecido = False
    def aposentar(self):
        if self.aposentado == False:
            self.aposentado = True
        else:
            print(f'{self.nome} já está aposentado.')
    def aquecer(self):
       if self.aposentado == False:
            if self.aquecido == False:
                print(f'{self.nome} Começou a aquecer.')
                self.aquecido = True
            else:
                print(f'{self.nome} já está aquecido.')
       else:
           print(f'{self.nome} está aposentado.')
class Ciclista(Atleta):
    def __inti__(self, nome, peso):
        super().__init__(nome, peso)
    def pedalar(self):
       if self.aquecido == False:
           print(f'O ciclista {self.nome} precisa se aquecer.')
       else:
           if self.aposentado == False:
               print(f'O ciclista {self.nome} foi pedalar.')
           else:
               print(f'O ciclista {self.nome} está aposentado.')
class Nadador(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    def nadar(self):
        if self.aquecido == False:
            print(f'O nadador {self.nome} precisa se aquecer.')
        else:
            if self.aposentado == False:
                print(f'O nadador {self.nome} foi nadar.')
            else:
                print(f'O nadador {self.nome} está aposentado.')
class Corredor(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    def nadar(self):
        if self.aquecido == False:
            print(f'O corredor {self.nome} precisa se aquecer.')
        else:
            if self.aposentado == False:
                print(f'O corredor {self.nome} foi correr.')
            else:
                print(f'O corredor {self.nome} está aposentado.')
class Tri(Nadador, Corredor, Ciclista):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)


