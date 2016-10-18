#coding=utf-8

import socket
import sys

def reuse_socket_addr():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the old state of the SO_REUSEADDR option
    old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print("Old sock state: ", old_state)

    # Enable the SO_REUSEADDR option
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Get the new state of the SO_REUSEADDR option
    new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print("New sock state: ", new_state)

    local_port = 8282
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(('', local_port))
    srv.listen(1)
    print("Listening on port: ", local_port)
    while True:
        try:
            connection, addr = srv.accept()
            print("Connected by %s:%s" % (addr[0], addr[1]))
        except KeyboardInterrupt:
            # "Ctrl + C" can kill this process
            break
        except socket.error as msg:
            print(msg)
    
    
    
if __name__ == "__main__":
    reuse_socket_addr()

# Test: telnet localhost 8282
