

import getpass
import sys
import telnetlib

host = raw_input("Router: ")
user = "rcp"
password = "rcp"

print "Connecting to router..."
tn = telnetlib.Telnet(host,23)
tn.read_until("User: ")
tn.write(user + "\n")
tn.read_until("Password: ")
tn.write(password + "\n")
tn.write("ena\n")
print "Fetching data..."
tn.write("config\n")
tn.write("copy startup-config tftpboot/pruebar1\n")
tn.write("exit\n")
tn.write("exit\n")
print "Printing output..."
print tn.read_all()