algoritmo "semnome"
// Fun��o :
// Autor :
// Data : 14/04/2014
// Se��o de Declara��es 
var
  i,numerador:inteiro
  soma:real
inicio
// Se��o de Comandos 
soma:=0
numerador:= 1000
para i de 50 ate 1 faca
     se ((1% 2)=0) entao
     soma:= soma +numerador/i
     senao
     soma := soma+numerador/i
     fimse
     numerador:=numerador-3
     escreval ("o valor dos primeiros 50 termos d a s�rie �: ",soma)

fimalgoritmo
