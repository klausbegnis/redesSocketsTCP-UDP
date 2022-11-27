from time import sleep
from socket import *
from random import randint

class BaseA(socket):
    def __init__(self,port):
        """Inicia o socket da BaseA"""
        super().__init__(AF_INET, SOCK_STREAM)
    
        """Atributos gerais"""
        self.PORT = port
        self.addrCentroDeComando = gethostbyname('localhost')
        self.TuplaDoCC = (self.addrCentroDeComando, self.PORT)

        """Mensagens possiveis"""
        self.socorro = "Acho que hoje chove".encode()
        self.pacifico = "O ceu esta tao limpo!".encode()

        """Estabelece conexão"""
        self.connect(self.TuplaDoCC)

        """Inicia simulacao"""
        self.simulacaoDoCliente()
    
    def enviaAviso(self,help):
        if help <= 0:
            print("Nao ha necessidade de auxilio")
            self.send(self.pacifico)
        else:
            print("Enviando pedido de ajuda")
            self.send(self.socorro)

    def simulacaoDoCliente(self):
        while True:
            infoAleatoria = randint(0,1)
            self.enviaAviso(help=infoAleatoria)
            sleep(5)
    
    def __del__(self):
        """Ao destruir a instancia fecha a conexao"""
        self.close()


BASEA = BaseA(5000)