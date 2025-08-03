import socket

class DirBrute():
	def __init__(self, target_url) -> None:
		self.target_url = target_url

	def parse_url(self, url):
		parts = url.split("/")

		protocol = parts[0]
		host = parts[2]
		path = ""

		for subroute in parts[3:]:
			path += "/" + subroute

		if path == "":
			path = "/"

		return (protocol, host, path)

	def send_http_get_request(self, path, host):
		request_string_template = "GET {} HTTP/1.1\r\nUser-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)\r\nHost: {}\r\nConnection: Keep-Alive\r\n\r\n"
		request_string = request_string_template.format(path, host)

		http_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		http_socket.connect((host, 80))

		http_socket.send(request_string.encode())
		response = http_socket.recv(4096)

		print(response)

	def parse_http_response(self, response_byte_string):
		response_code = ""
		headers = ""
		html = ""

		return (response_code, headers, html)

def test():
	# test init
	tdb = DirBrute("http://scanme.org")

	# test parse_url
	print(tdb.parse_url("http://scanme.org"))

	# test parse_http_response

	# test send_http_get_request

	tdb.send_http_get_request("/", "scanme.org")

test()
