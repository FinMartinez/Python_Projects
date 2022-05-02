#Helper file to generate a random string of integers for a mock-IP address

import random   #standard library to generate pseudo-random numbers
import socket   #standard library used for low-level network interfaces
import struct   #standard library used for translating Py values and C structs

def IP_gen():
    #socket.inet_ntoa is used to generate a quad-string IP address
    #struck.pack returns a string from format argument and v1 arg
    #random.randint generates a random hex integer betwwn 1 and 0xffffffff
    address = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    return address
#apparently this works?