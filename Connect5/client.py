import socket
import pickle


class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 'localhost' #'140.203.229.105' #'192.168.0.10'
        self.port = 5555
        self.addr = (self.host, self.port)
        self.grid = self.connect()
        #self.grid = pickle.loads(self.id)

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(4096*2)

    def send(self, data):

        try:
            self.client.send(pickle.dumps(data))
            #self.client.send(str.encode(data))
            reply = pickle.loads(self.client.recv(4096*2))
            return reply
        except socket.error as e:
            return str(e)
