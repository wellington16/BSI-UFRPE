algoritmo "semnome"
// Fun��o :
// Autor :
// Data : 15/04/2014
// Se��o de Declara��es 
var
preco,valor,moeda:real
opcao:inteiro
escolheu:logico
inicio
// Se��o de Comandos 
escolheu:=falso
enquanto escolheu =falso faca
         escreval("1-Coca R$2,30")
         escreval("1-Fanta R$1,90")
         escreval("1-Soda R$1,70")
         leia (opcao)
        se opcao =1 ent�o
            preco :=2,30
            escolheu := verdadeiro
          senao
             se opcao =2 ent�o
            preco :=1,95
            escolheu := verdadeiro
         senao
            se opcao =3 ent�o
            preco :=1,70
            escolheu := verdadeiro
         senao
         escreval("Op��o Inv�lida")
         fimse
        fimse
       fimse
fimenquanto
valor:=0
enquanto ((preco-valor)>0)faca
escreval ("Digite uma moeda")
leia (moeda)
se (moeda=0,05)ou(moeda=0,25)ou(moeda=0,50)ou(moeda=1,00)entao
valor := valor +moeda
senao
escreval("moeda Invalida")
fimse
fimenquanto
escreval (("troco: ",preco-valor)*-1)
fimalgoritmo
