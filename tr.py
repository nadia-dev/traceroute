import socket
import argparse


def main():
    parser = argparse.ArgumentParser(description='specify hostname')
    parser.add_argument('-host', help = 'specify hostname', type = str, dest = 'host')
    args = parser.parse_args()
    host = args.host
    
    if host == None:
        print 'Specify hostname'
        exit(0)
        
    traceroute(host)


def traceroute(host):

    n = 1
    listen = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
    
    while True:
        conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        conn.setsockopt(socket.SOL_IP, socket.IP_TTL, n)
        n += 1
        conn.connect((socket.gethostbyname(host), 33434))
        conn.send('happy')
        conn.close()
    
        address = listen.recvfrom(4096)[1][0]
        if address != socket.gethostbyname(host):
            print address
        else: 
            break
        
    listen.close()
        
if __name__ == '__main__':
    main()

