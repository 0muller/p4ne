from email.policy import strict
from ipaddress import IPv4Network
import random

class IPv4Ranbom (IPv4Network):
    def __init__(self, ip_start=0, ip_end=24):
        IPv4Network.__init__(self, (random.randint(0x0b000000,0xdf000000),random.randint(ip_start, ip_end)),strict=False)
        #IPv4Network.__init__(self, ip_start, ip_end)
    def regular(self):
        return self.is_global and not (self.is_multicast or self.is_link_local or self.is_loopback or self.is_private or self.is_reserved or self.is_unspecified)

    def key_value(self):
        return int(self.network_address) + (int(self.network_address) << 24)

    def sortf(x):
        return x.key_value()

    random.seed()
#rnlist = []
i=0
while i < 10:
    net1 = IPv4Ranbom(10,12)
    print(net1)
    i=i+1

#while len(rnlist) < 50:
 #   random_network = IPv4Ranbom(10,24)
  #  if random_network.regular() and random_network not in rnlist:
   #     rnlist.append(random_network)
#print (rnlist)

