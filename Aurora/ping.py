import os
import time

def ping(host):

    start_time = time.time()

    os.popen("ping -c1 " + host)

    return time.time() - start_time
    
