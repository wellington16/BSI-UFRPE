# -*- coding: utf-8 -*-

import random
from socket import *

def connection(ip,port):
  global cnt
  cnt = 0
  clientSocket = socket(AF_INET, SOCK_STREAM)
  clientSocket.connect((ip,port))
  return clientSocket

def hardClose(sckt):
  sckt.close()

def softClose(sckt):
  global cnt
  sckt.send(str(cnt)+" TERM")
  cnt += 1
  data, addr = sckt.recvfrom(2048)
  mess = data.strip("\n").split(" ")
  if (mess[1] == "OK"):
    sckt.close()
    print("TERM is OK!")
  else:
    print("Error in TERM!")
    sckt.close()

#test acknowledgment phase
#bad = 1 iff the user does not exist
#bad = 0 iff the user exists
def test1(sckt, user, bad):
  global cnt
  mesagem = str(cnt)+" CUMP "+user
  sckt.send(mesagem.encode('ascii'))
  cnt += 1
  data, addr = sckt.recvfrom(2048)
  mess = data.decode('ascii').strip("\n").split(" ")
  print(mess)
  if len(mess) != 2:
    return -2
  if (not int(mess[0]) == cnt-1):
    return -2
  if (mess[1] == "OK"):
    return -1 if bad == 1 else 1
  elif (mess[1] == "NOK"):
    return 1 if bad == 1 else -1
  else:
    return -2

#test not expected commands
def test2(sckt):
  global cnt
  mensagem = str(cnt) + " TRAP"
  sckt.send(mensagem.encode('ascii'))
  cnt += 1
  data, addr = sckt.recvfrom(2048)
  mess = data.decode("ascii").strip("\n").split()
  print(mess)
  if len(mess) != 2:
    return -2
  if (not int(mess[0]) == cnt-1):
    return -2
  if (mess[1] == "NOK"):
    return 1
  else:
    return -1

#test list phase
def test3(sckt):
  global cnt
  mensagem = str(cnt) + " LIST"
  sckt.send(mensagem.encode('ascii'))
  cnt += 1
  data1 = ""
  commandUnknow = True
  fileCnt = 0

  while 1:
    data, addr = sckt.recvfrom(2048)
    # print(data)
    if commandUnknow:
        try:
            commandUnknow = False
            splitteddata = data.decode("ascii").split(" ")
            # print(splitteddata)
            if splitteddata[1] == "ARQS":
                 # print(splitteddata[2])
                 filesTotal = len(splitteddata[2])
                 # print(len(splitteddata[2]))
                 fileCnt += len(data.decode("ascii").split(","))
                 # print(fileCnt)
            #     print(fileCnt)
        except Exception as e:
            print (e)
            break
    else:
        fileCnt += len(data.decode("ascii").split(","))
    data1 += data.decode("ascii")
    if fileCnt >= filesTotal:
        break

  # print(data1)
  files = data1.split(",")
  firstFile = files[0].split(" ",3)
  # print(files[0].split(" ",3))
  files[0] = firstFile[2]
  mess = data1.split(" ")
  if len(mess) < 4:
    return (-2,"")
  if (not int(mess[0]) == cnt-1):
    return (-2,"")
  if (mess[1] == "ARQS"):
    return (1,files)
  elif (mess == "NOK"):
    return (0,"")
  else:
    return (-2,"")

#test arq phase
def test4(sckt,arq,bad):
  global cnt
  mensagem = str(cnt) + " PEGA " + arq
  sckt.send(mensagem.encode('ascii'))
  cnt += 1
  data1 = ""
  commandUnknow = True
  byteCnt = 0
  data2 = None
  bytesTotal = None
  while 1:
    data, addr = sckt.recvfrom(2048)
    if commandUnknow:
        try:
            commandUnknow = False
            splitteddata = data.split(" ",3)
            print(splitteddata)
            print(splitteddata[1])
            print(splitteddata[1])
            if splitteddata[1] == "ARQ":
                print(splitteddata[2])
                bytesTotal = (splitteddata[2])
                data2 = splitteddata[3]
                byteCnt += len(data2)
            elif "NOK" in data:
                data1 += data
                break
        except Exception as e:
            print (e)
            break
    else:
        data2 += data
        byteCnt += len(data)
    data1 += data
    print(byteCnt,bytesTotal)
    if byteCnt >= bytesTotal:
        break

  if data2:
    f = open(arq,"w")
    f.write(data2)
    f.close()

  mess = data1.split(" ",3)
  if bad == 0 and len(mess) < 4:
    return -2
  if bad == 1 and len(mess) < 2:
    return -2
  if (not int(mess[0]) == cnt-1):
    return -2
  if (mess[1] == "ARQ"):
    return -1 if bad == 1 else 1
  elif (mess[1] == "NOK"):
    return 1 if bad == 1 else -1
  else:
    return -2

if __name__ == "__main__":
  # if len(sys.argv) <= 3:
  #   print("Usage: pta-client.py <server-ip> <server-port> <user>")
  #   sys.exit(2)
  serverIp = '127.0.0.1'
  serverPort = 50007
  user = 'wellington'

  points = 0

  #Testing bad command
  print("Testing command without CUMP")
  cSocket = connection(serverIp,serverPort)
  points += test2(cSocket)
  print("Points: %d/6" % points)
  hardClose(cSocket)

  #Testing bad CUMP command
  print("Testing CUMP with bad user")
  cSocket = connection(serverIp,serverPort)
  points += test1(cSocket,"",1)
  print("Points: %d/6" % points)
  hardClose(cSocket)

  # #Testing good CUMP command
  print("Testing CUMP with good user")
  cSocket = connection(serverIp,serverPort)
  points += test1(cSocket,user,0)
  print("Points: %d/6" % points)

  # Testing LIST
  print("Testing LIST")
  # cSocket = connection(serverIp, serverPort)
  (pts,arqs) = test3(cSocket)
  points += pts
  print("Points: %d/6" % points)
  arq = random.choice(arqs)
  print(arq)

  # #Testing ARQ
  print("Testing ARQ with good file")
  cSocket = connection(serverIp, serverPort)
  if arq:
      print(type(arq))
      points += test4(cSocket,arq,0)
  else:
      points += -2
  print("Points: %d/6" % points)
  #
  #Testing ARQ
  # print("Testing ARQ with bad file")
  # points += test4(cSocket,"wellington",1)
  # print("Points: %d/6" % points)
  #
  # #Testing TERM
  # print("Testing TERM")
  # softClose(cSocket)
