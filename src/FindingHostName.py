import os
import socket

myhost=raw_input()
getmyhost=socket.gethostname()
getmyipaddr=socket.gethostbyname(getmyhost)
getmyfqdn=socket.getfqdn()
#mydomainname=
#getmymyhost=socket.gethostname(myhost)
getmymyipaddr=socket.gethostbyname(myhost)
getmymyfqdn=socket.getfqdn(myhost)
print getmyhost, "\n", getmyipaddr,"\n",getmyfqdn,"\n"
print "\n",getmymyipaddr,"\n",getmymyfqdn

