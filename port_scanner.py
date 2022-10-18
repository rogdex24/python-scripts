"""
RUN and Test it
"""

import socket
import threading
from queue import Queue

# gethosname - localhost
target = socket.gethostname() # could be any IP
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Make TCP Connection
        sock.connect((target, port))

        # If connection is made port is open
        return True

    except:
        # If TCP Connection fails, port is NOT open
        return False

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    # All threads process through the queue to avoid checking one port multiple times
    while not queue.empty():
        port = queue.get()
        if portscan(port) == True:
            print(f"Port {port} is open!")
            open_ports.append(port)

port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

# Creating 100 threads
for t in range(100):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

# wait for all threads to complete
for thread in thread_list:
    # waiting for a thread to complete : blocker method .join
    thread.join()

print("Open ports are: ", open_ports)



# This runs very slow, hence threading is used in above approach
"""
for port in range(1, 1024):
    result = portscan(port)
    if result == True:
        print(f"Port {port} is open !")
    else:
        print(f"Port {port} is closed")
"""

