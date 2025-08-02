import string

chars = string.ascii_lowercase

p = ""

for c in chars:
	for i in range(0, 10):
		for n in range(0, 10):
			p += c + str(i) + str(n)

print(p)
