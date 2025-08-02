import scanner
import cli

(silent, target, method) = cli.get_arguments()
cli.print_logo()
s = scanner.Scanner(target, silent)

if method.upper() == "TCP":
    s.tcp_scan()
elif method.upper() == "SYN":
    s.syn_scan()
elif method.upper() == "ACK":
    s.ack_scan()
elif method.upper() == "FIN":
    s.fin_scan()

