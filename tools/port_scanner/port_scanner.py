import socket
import sys
import errno

#check if the number of arguments is right either 4 or 5 with printing only open ports option!
if len(sys.argv) not in (4, 5):
    print("Usage: python3 p_scanner.py <host> <start_port> <end_port> [--open]")
    sys.exit(1)

#if #arguments is 5 we check if the last one is --open otherwise we print usage error.
only_open = False
if len(sys.argv) == 5:
    if sys.argv[4] == '--open':
        only_open = True
    else:
        print("Usage: python3 p_scanner.py <host> <start_port> <end_port> [--open]")
        sys.exit(1)

#we check if all values are right
try:
    host = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
except ValueError:
    print("Error: Enter a port number (integer)")
    sys.exit(1)

#we iterate through the range of ports and try to establish a connection with each of them.
for port in range(start_port, end_port+1):
    s = socket.socket() #a socket needs a port and a host
    s.settimeout(1)
    result = s.connect_ex((host, port))
    s.close()

    #we check the cases of the returned number of s.connect_ex
    if only_open and result != 0:
        continue
        #don't print nothing since no port is open
    elif result == 0:
        print(f"port {port} is open!")
    elif result == errno.ECONNREFUSED:
        print(f"port {port} is closed!")
    elif result == errno.EAGAIN:
        print(f"port {port} is filtered")
    else:
        print(f"Error on port {port} (code{result})")

    