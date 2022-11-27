from socket import *

class CentroDeComando(socket):
    def __init__(self,thisPort,baseB_PORT,maxConnection) :
        """Inicia o socket do servidor na prota 5000"""
        super().__init__()
        self.PORT = thisPort
        self.bind(('',self.PORT))

        self.conexoesConquistadas = 0

        """Os clientes abrem a conexao e por conta da sensbilidade dos dados
        e da necessidade de resposta imediata o servidor"""
        self.baseA = None
        

        """Limita número de conexões simultâneas"""
        self.listen(maxConnection)

        # 0 -> base A requer reforco aereo
        # 1 -> base A nao necessita de ajuda
        self.translator =  {"Acho que hoje chove" : 0,
                            "O ceu esta tao limpo!" : 1}

        """Conecta-se com o servidor UDP da base B (vira cliente p/ base B)"""
        # Classe CentroDeComando herda socket e o inicia como tcp super().__init__()
        # ainda assim, possui um atributo que é sua conexão UDP com a base B
        self.baseB = socket(AF_INET,SOCK_DGRAM)
        self.baseB_PORT = baseB_PORT
        self.baseB_addr = ("127.0.0.1", self.baseB_PORT)

        """Inicia execucao do servidor"""
        self.runServer()

    def waitForConnections(self):

            receivedConnection, endereco = self.accept()

            # aqui no caso pratico testaria se o endereco e o 
            # da base e atribuiria para cada self.clientX o
            # socket correto, porem, como executei no mesmo computador
            # todos os clientes que executar estarao no proprio localhost

            # apenas simulando que ninguem conseguiria descobrir o 
            # ip do servidor, distribuo em ordem de chegada para os
            # atributos de cliente

            print("Connectado com: ",endereco[0], "Socket: ", endereco[1])
            
            if self.conexoesConquistadas == 0:
                self.baseA = receivedConnection
                self.conexoesConquistadas = 1
            else:
                self.baseB = receivedConnection
    
    def selfDecodeMsg(self,msg):

        """Traduz mensagem recebida da base A"""

        msgDecoded = msg.decode('utf-8')

        try: 
            msgDecoded = self.translator[msgDecoded]
        except:
            msgDecoded = None
        return msgDecoded

    def runServer(self):
        while True:
            # primeiro ambas estacoes precisam estar conectadas
            if not(self.baseA):
               self.waitForConnections()
            # com as conexos realizadas
            else:
                # como a base A esta no fronte, trata-se suas informacoes
                # primeiramente e por necessitar saber se sua base esta
                # recebendo essas informacoes, utiliza-se TCP
                msgDaBaseA = self.baseA.recv(1024)
                msgDaBaseA = self.selfDecodeMsg(msgDaBaseA)

                if msgDaBaseA == 0:
                    print("Base A em apuros!")
                    self.baseB.sendto("Os ventos sao favoraveis".encode() , self.baseB_addr)
                elif msgDaBaseA == 1:
                    print("Base A em situacao pacifica")
                    self.baseB.sendto("Uma tempestade se aproxima".encode(), self.baseB_addr)


serivdor = CentroDeComando(5000,2500,1)
