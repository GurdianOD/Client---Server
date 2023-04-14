import socket
import threading
ip = '127.0.0.1'
port1 = 5230
port2= 5231

def get_data1():
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.connect((ip , port1))
    data1 = s1.recv(1024)
    print(data1)
    s1.close()

def get_data2():
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect((ip , port2))
    data2 = s2.recv(1024)
    print(data2)
    s2.close()

threading.Thread(target=get_data1).start()
threading.Thread(target=get_data2).start()
