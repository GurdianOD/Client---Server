import socket
import threading
ip = '127.0.0.1'
port1 = 5230
port2= 5231

def send_data1():
    tcpSocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSocket1.bind((ip , port1))
    tcpSocket1.listen()
    print("server1 is listening")
    client, addr = tcpSocket1.accept()
    client.send(b"data1")
    client.close()

def send_data2():
    tcpSocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSocket2.bind((ip , port2))
    tcpSocket2.listen()
    print("server2 is listening")
    client, addr = tcpSocket2.accept()
    client.send(b"data2")
    client.close()

threading.Thread(target=send_data1).start()
threading.Thread(target=send_data2).start()
