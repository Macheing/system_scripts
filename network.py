#!/usr/bin/env python3
import requests
import socket

def check_localhost():
        localhost = socket.gethostbyname('localhost')
        #print('Localhost:',localhost)
        if localhost == "127.0.0.1":
                return True
print('Localhost:',check_localhost())

def check_connectivity():
        request = requests.get("http://www.google.com")
        if request.status_code == 200:
                return True

print("Connected to google.com:",check_connectivity())
