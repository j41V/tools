import requests
import sys
import threading

if len(sys.argv) != 3:
    print("usage: dirbrute.py [URL] [WORDLIST]")
    exit()

url = sys.argv[1]
threads = []
routes = set()
status_codes = [200, 301, 400, 405]

count = 1

wordlist_len = len(open(sys.argv[2]).readlines())

def test_route(route, count):
    print("[*]Scanning route ({}/{})".format(count, wordlist_len), end="\r")
    req = requests.get(route)

    if req.status_code in status_codes:
        routes.add(route)

with open(sys.argv[2]) as wf:
    for word in wf.readlines():
        route = ""

        if url.endswith("/"):
            route = url + word.strip()
        else:
            route = url + "/" + word.strip()

        t = threading.Thread(target=test_route, args=(route, count))
        threads.append(t)
        count += 1


for t in threads:
    t.start()

for t in threads:
    t.join()

print(routes)

