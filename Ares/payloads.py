import string
import random
from typing import List, Self

"""

payloads:

generic: A*4000

random: string with random chars

"""

class Payload():
	def __init__(self, chars):
		self.chars = chars

	def get_chars(self):
		return self.chars

class Generic(Payload):
	def __init__(self, length=4000, char="A"):
		super().__init__(char*length)

class Random(Payload):
	def __init__(self, length=4000, chars=string.printable):
		p = ""
		for n in range(0, length):
			p += chars[random.randrange(0, len(chars))]
		super().__init__(p)

class Hybrid(Payload):
	def __init__(self, payload_1=Random(), payload_2=Generic()):
		p = Custom(payload_1.get_chars() + payload_2.get_chars())
		super().__init__(p.get_chars())

class Custom(Payload):
	def __init__(self, chars):
		super().__init__(chars)

	def from_file(filename):
		with open(filename) as payload_file:
			chars = payload_file.read().strip("\n")
			return Custom(chars)

class PayloadList():
	def __init__(self, payloads) -> None:
		self.payloads = payloads

class All(PayloadList):
	def __init__(self) -> None:
		super().__init__([Generic(), Random(), Hybrid()])

		#self.payloads = [Generic().get_payload(), Random().get_payload()]

class CustomList(PayloadList):
	def __init__(self, payloads: List) -> None:
		super().__init__(payloads)


