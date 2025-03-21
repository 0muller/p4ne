
from pysnmp.hlapi import *

result = getCmd(SnmpEngine(),
                CommunityData('public', mpModel=0),
                UdpTransportTarget(('10.31.70.209', 161)),
                ContextData(),
                ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
                )

print (result[1])
#for request in result[3]:
 #   print(request)






