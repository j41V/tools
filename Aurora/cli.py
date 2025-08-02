import sys

LOGO = r"""
                 (        )   (              
   (             )\ )  ( /(   )\ )    (      
   )\        (  (()/(  )\()) (()/(    )\     
((((_)(      )\  /(_))((_)\   /(_))((((_)(   
 )\ _ )\  _ ((_)(_))    ((_) (_))   )\ _ )\  
 (_)_\(_)| | | || _ \  / _ \ | _ \  (_)_\(_) 
  / _ \  | |_| ||   / | (_) ||   /   / _ \   
 /_/ \_\  \___/ |_|_\  \___/ |_|_\  /_/ \_\  
"""

USAGE = "usage: aurora [OPTIONS] [SCAN METHOD] [TARGET]\nSupported scan methods:\nTCP | SYN | ACK | FIN\ndefault is tcp\nOptions:\n-s/--silent | only print results and NO runtime information"

def print_logo():
    print(LOGO)

def print_usage():
    print(USAGE)
    exit()

def get_arguments():
    if "-h" in sys.argv or len(sys.argv) == 1 or len(sys.argv) > 3:
        print_usage()
        
    if len(sys.argv) == 2:
        return (False, sys.argv[1], "TCP")
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-s" or sys.argv[1] == "--silent":
            return (True, sys.argv[2], "TCP")
        return (False, sys.argv[2], sys.argv[1])
    else:
        print_usage()
