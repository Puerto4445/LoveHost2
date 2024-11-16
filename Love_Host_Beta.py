import scapy.all as scapy
import argparse

def argparse_argument():
    parser = argparse.ArgumentParser(description="Escaner de nodos en la red (ARP)")
    parser.add_argument("-t","--target",required=True,dest="target",help="Host/ IP range to Scan")
    arg = parser.parse_args()
    return arg.target

def Scan_ip(ip):
    arp_packet = scapy.ARP(pdst= ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet= broadcast_packet/arp_packet
    answered,unanswered = scapy.srp(arp_packet,timeout=2, verbose= False, )                 
    response = answered.summary()
    if response:
        print(response)
def main():
    ip = argparse_argument()
    Scan_ip(ip)

if __name__=="__main__":
    main()