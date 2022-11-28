from time import sleep
from socket import *
from random import randint

class BaseB(socket):
    def __init__(self,port):
        """Inicia o socket da BaseA"""
        super().__init__(AF_INET, SOCK_DGRAM)
        self.PORT = port
        self.bind(("",self.PORT))
    
        """Atributos gerais"""
        

        """Mensagens possiveis"""
        self.translator = {
            "Os ventos sao favoraveis" : 0, # base A em apuros
            "Uma tempestade se aproxima" : 1 # base A nao necessita de ajuda
        }

        self.frotaAereaOcupada = False

        """Inicia simulacao"""
        self.runServer()

    def decodeMsg(self,msg):

        """Traduz mensagem recebida do centro de comando"""

        msgDecoded = msg.decode('utf-8')

        try: 
            msgDecoded = self.translator[msgDecoded]
        except:
            msgDecoded = -1
        return msgDecoded

    def runServer(self):
        while True:
            msg, client = self.recvfrom(1024)
            
            translatedMessage = self.decodeMsg(msg)

            if translatedMessage == 0:
                print("Base A em apuros, enviando frota aerea!")
                if not(self.frotaAereaOcupada):
                    self.enviaFrotaAerea()
                else:
                    print("Frota aerea ja esta a caminho")
            elif translatedMessage == 1:
                print("Situacao calma na base A")
                if self.frotaAereaOcupada:
                    self.retornaFrotaAerea()
                else:
                    print("Frota ja esta na base")
    
    def enviaFrotaAerea(self):
        self.frotaAereaOcupada = True
        print(f"Enviando frota aerea")
    def retornaFrotaAerea(self):
        self.frotaAereaOcupada = False
        print(f"Frota aerea retornando a base")

BASEA = BaseB(2500)