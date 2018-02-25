import socket
import datetime
import os
import re
import sys
import subprocess
import pyasn


def lookup(addr):
     try:
         return socket.gethostbyaddr(addr)
     except socket.herror:
         return None, None, None

         


ip_name_formatted = "input_IP_Data.txt"

#Takes the GAWK file output - and strips out any data apart from IP address
with open(ip_name, 'r') as f, open(ip_name_formatted, 'w') as n:
    for line in f:
        new_line = re.sub('[^a-zA-Z0-9_. ]+', ' ', line)
        n.write(new_line+'\n')

input_data_file = "no_dup_ip.txt"
dns_records = "netstat_data_all_bridges_dns_records.txt"




with open(input_data_file, 'r') as f, open(dns_records, 'w') as n:
    for line in f:
        if line.strip() == "0.0.0.0":
              pass
          else:
              name,alias,addresslist = lookup(line.strip())
              print name
              n.write('{"Name": "' + name + '", "alias": "' + alias + '", "addresslist": "' +addresslist +'"}\n')

              #n.write(output)
         #            # sys.exit()
         #        # n.write(new_line+'\n')


#name,alias,addresslist = lookup('4.2.2.2')
