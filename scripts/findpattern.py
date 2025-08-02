import sys
import string

if len(sys.argv) != 2:
	print("usage: find_pattern.py [pattern] | important: pattern has to be one lowercase ascii letter and to digits")
	exit()

chars = sys.argv[1]
letter = chars[0]
digits = chars[1] + chars[2]
t = string.ascii_lowercase.find(letter)
o = str(t) + digits
e = int(o) * 3
print(e)