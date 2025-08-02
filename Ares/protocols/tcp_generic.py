import socket

class TcpGeneric():
	def __init__(self, payload, ip ,port) -> None:
		self.payload = payload
		self.ip = ip
		self.port = port

	def send(self):

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((self.ip, self.port))
		s.send(self.payload.get_chars().encode())
