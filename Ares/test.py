import ares

p = ares.payload.Generic()

print(p.get_payload())

print(ares.payload.Random().get_payload())

print(ares.payload.All().payloads)

print(ares.payload.CustomList([p.get_payload()]).payloads)