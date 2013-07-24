#!/usr/bin/python

import socket
import argparse
import time
import pygeoip
  
gi = pygeoip.GeoIP('geo/GeoLiteCity.dat')


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
    roundtrips = []
    query = 3
    ttl = 1
      
    while True:
        listen = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
          
        while query != 0:        
                
            conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            conn.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
            conn.connect((socket.gethostbyname(host), 33434))
            conn.send('happy')
            conn.close()
              
            send_time = time.time()
            address = listen.recvfrom(4096)[1][0]
            recv_time = time.time()
            roundtrip = str(round((recv_time - send_time) * 1000, 3)) + ' ms'
            roundtrips.append(roundtrip)
            query -= 1
              
        if address != socket.gethostbyname(host): 
            rec = gi.record_by_name(address) 
            if rec:   
                city = rec['city']
                country = rec['country_name']
            else:
                city = 'unknown city'
                country = 'unknown country'          
            print ttl, address, city, country, roundtrips
        elif address == socket.gethostbyname(host): 
            print str(ttl) + ' Arrived to ' + host 
            break
            
        listen.close()
          
        ttl += 1
        query = 3
        roundtrips = []
      
          
if __name__ == '__main__':
    main()
