#imprime os 15 primeiros n�meros primos
print "Este programa imprime os primeiros 15 n�meros primos, s�o eles:"
quantidadePrimos = 0
i = 2
while quantidadePrimos < 15:
    #verificando se o "i" � primo:
    x = 2 #primeiro divisor a ser verificado
    while x < i: #repetindo para todos os antecessores de "i"
        if (i%x) == 0: #conseguiu dividir (� divisor), ent�o o "i" n�o � primo
            break
        x += 1
    else: #fez todas as divis�es pelos antecessores no "while" e o n�mero � primo (n�o dividiu por ningu�m)
        quantidadePrimos += 1 #conta o n�mero primo
        print i, "quantidade: ", quantidadePrimos #o n�mero i � primo, ent�o escreve na tela
    i += 1
