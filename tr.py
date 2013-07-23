import socket
import argparse
import time

query = 3
ttl = 1

def main():
    
    parser = argparse.ArgumentParser(description='traceroute')
    parser.add_argument('-host', help = 'specify hostname', type = str, dest = 'host')
    args = parser.parse_args()
    host = args.host
    
    if host == None:
        print 'Specify hostname'
        exit(0)
                
    traceroute(host)


def traceroute(host):
    timestamps = []
    global query, ttl
    
    while True:
        
        listen = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
        while query != 0: 
                   
            conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            conn.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
            conn.connect((socket.gethostbyname(host), 33434))
            conn.send('happy')
            conn.close()
            
            sent_time = time.time()
            address = listen.recvfrom(4096)[1][0]
            recieved_time = time.time()
            actual_time = recieved_time - sent_time
            timestamp = str(round(actual_time*1000, 3)) + ' ms'
            timestamps.append(timestamp)
            query -= 1
        
        if address != socket.gethostbyname(host):
            print address, timestamps
        else: 
            break 
          
        listen.close()
        
        ttl += 1
        query = 3
        
        timestamps = []
        
        
if __name__ == '__main__':
    main()

