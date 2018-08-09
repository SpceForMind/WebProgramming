
import socket

close_conection = "close"

def my_send(sock, msg):
    total_len = 0
    while total_len < len(msg):
        sent = sock.send(msg[total_len:])
        if sent == 0:
            raise RuntimeError("brocke")
        total_len += sent

'''
    create object <socket>
    AF_INET - work with web sockets
    SOCK_STREAM - work with TCP
'''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(sock)
sock.bind(("127.0.0.1", 1234))
sock.listen(10)
'''
    echo-server
'''
while True:
    conn, addr = sock.accept() #accept next client
    while True:
        data = conn.recv(1024)
        if not data or data.decode() == close_conection:
            break
        my_send(conn, data)
    conn.close()
