#This program de-fangs an IP address. 
#A randomly generated IP address is gathered from IP_generator.py
#This program takes that random IP and de-fangs it.

#imports
from IP_generator import IP_gen

#Driver method
print("Please wait for IP address to be generated")
IP_address = IP_gen()
print("IP address to be de-fanged is:" + IP_address)

#Begin De-Fanging
def de_fanger(address):
    new_address = ""
    split_address = address.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address
de_fangedIP = de_fanger(IP_address)
print("De-fanged IP address is: " + de_fangedIP)
print("Thank you for using IP De-Fanger")

#end