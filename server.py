#!/usr/bin/env python
# 
# Ranswomware Script Version 1.0.1 (2022)
#
# This tool may be used for legal purposes only.  Users take full responsibility
# for any actions performed using this tool. The author accepts no liability for
# damage caused by this tool.  If these terms are not acceptable to you, then do 
# not use this tool.
# 
# by Pierre CHAUSSARD
# 
# 10-Feb-2022 - 1.0.0 - Creating ransomware.
# 14-Feb-2022 - 1.0.1 - Adding server.


import socket

s = socket.socket()
print("Socket successfully created")

port = 55655

s.bind(('', port))
print("socket binded to %s" %(port))

s.listen(5)
print("socket is listening")

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Thank you for connecting'.encode())
    c.close()
    break