from scapy.all import *

packet = IP(dst="10.15.4.156") / ICMP()

response = sr1(packet, timeout=2)

if response:
    response.show()
else:
    print("no")
