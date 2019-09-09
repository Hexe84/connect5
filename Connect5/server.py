import socket
from _thread import *
import sys
import pickle
import ConnectFive as game

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'localhost' # '140.203.229.105' #'192.168.0.10'
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

turn = -1

#def threaded_client(conn, grid):
def threaded_client(conn):   

    #conn.send(str.encode(turn))
    reply = ''
    while True:
        try:
            data = conn.recv(4096).decode()
            #reply = data.decode('utf-8')
            if not data:
                break
            else:
                turn += 1
                # turn always 0 or 1
                turn = turn % 2

            #conn.sendall(str.encode(reply))
            conn.sendall(pickle.dumps(grid))
        except:
            break

    print("Connection Closed")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    #grid = game.grid
    start_new_thread(threaded_client, (conn,))