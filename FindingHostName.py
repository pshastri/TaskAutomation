import os
import socket

myhost=socket.gethostname()
myipaddr=socket.gethostbyname(myhost)
print myhost, "\n", myipaddr

