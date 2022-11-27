# Trabalho de Redes de Comunicação para Automação Industrial (DAS 5314)

## Estações militares e suporte aéreo

O trabalho consta no desenvolvimento da comunicação entre uma base no "fronte", dada como "Base A", um Centro de Comandos e uma "Base B (aerea)".

A Base A se comunica com o Centro de Comandos via TCP, enquanto o Centro de Comando se comunica com a Base B por UDP. Optou-se desta forma, pois, para os soldados da Base A seria interessante estabelecer uma conexão mais segura com o Centro de Comandos, evitando o acesso de terceiros não autorizados, gerando uma linha mais segura, já que é imprescindível que os soldados da Base A consigam se comunicar com o alto escalão do exército. Como o Centro de Comandos e a Base B são próximas e longe do alcance do inimigo, uma conexão UDP foi adotada, uma vez também que o Centro de Comandos não se interesa no caso da Base B receber as instruções, já que poderia, de outra forma iniciar as operações por conta própria. (esse último ponto não foi de interesse para fazer no trabalho, uma opção seria do Centro de Comandos esperar alguns segundos, se não houver decolagem de aviões avistadas, envia a mensagem novamente, alongaria muito o desenvolvimento). Em resumo, a ideia é da base A enviar sinais de socorro ou de situações controladas, fazendo com que o centro de comandos envia mensagens para a Base B, ordenando o envio das frotas ou o recuo das mesmas. Além disso, para simular o contexto militar, as mensagens são codificadas, necessitando das bases saberem um protocolo de tradução e reação.

## Utilização

Para testar o projeto, basta executar cada um dos arquivos .py, de forma que o 'baseA.py' seja executado por último, já que necessita encontrar o servidor.

## Video demonstrativo

... adicionar link do vídeo