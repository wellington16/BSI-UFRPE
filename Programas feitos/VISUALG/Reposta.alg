algoritmo "JOGO  de encontra a resposta correta"
// Fun��o :
// Autor :
// Data : 11/04/2014
// Se��o de Declara��es
var
Action1,Action2:inteiro
inicio
// Se��o de Comandos
escreval ("Qual a resposta esta correta?")
escreval ("Resposta UM!")
escreval ("Resposta DOIS")
escreval ("Resposta TRES")
leia (Action1)
escolha (Action1)
caso 1
   escreval ("Voc� acertou!")
   escreval ("precione ESC+F9 para reiniciar ou apenas ESC para sair.")
caso 2
     escreval ("Voc� errou!")
     escreva ("precione ESC+F9 para reiniciar ou apenas ESC para sair.")
fimalgoritmo
caso 3
     escreval ("Voc� errou!")
     escreval ("precione ESC+F9 para reiniciar ou apenas ESC para sair.")
fimalgoritmo
outrocaso
         escreval ("precione ESC+F9 para reiniciar ou apenas ESC para sair.")
fimalgoritmo
fimescolha
//fim da primeira pergunta
limpatela
escreval ("A resposta correta da questao 1 era : N�mero 1")
escreval("Parabens por voc� ter acertado a primeira pergunta!")
escreval("A segunda pergunta �: Qual a reposta correta?")
escreval ("Resposta UM!")
escreval ("Resposta DOIS")
escreval ("Resposta TRES")
leia (Action2)
se Action2=3 entao
escreval ("Voc� acertou!")
escreval ("precione ESC+F9 para reiniciar ou apenas ESC para sair.")
fimalgoritmo
se (Action2=2) ou (Action2=1)entao
escreval("Voc� errou!")
escreval ("precione ESC+F9 para reiniciar ou apenas ESC para sair.")
fimalgoritmo
fimse
fimse
caso 1
     escreval ("Voc� errou!")
escreval ("precione ESC+F9 para reiniciar ou apenas ESC para sair.")
fimescolha
fimalgoritmo
caso 2
     escreval ("Voc� errou!")
     escreval ("precione ESC+F9 para reiniciar ou apenas ESC para sair.")
     fimescolha
fimalgoritmo
caso 3
     escreval ("Voc� acertou!")
outrocaso
         escreval ("precione ESC+F9 para reiniciar ou apenas ESC para sair.")
fimalgoritmo
