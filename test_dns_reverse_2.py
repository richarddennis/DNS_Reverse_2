import datetime
import os
import re
import sys
import subprocess
#import pyasn
import socket 

def lookup(addr):
     try:
         return socket.gethostbyaddr(addr)
     except socket.herror:
         return "", "", "" 

def nontype(type_test):
    if type_test is None:
	return ""
    else:
	return type_test

ip_name = "input_IP_Data.txt" 
ip_name_formatted = "no_dup_ip.txt"
#Takes the GAWK file output - and strips out any data apart from IP 
#address
with open(ip_name, 'r') as f, open(ip_name_formatted, 'w') as n:
    for line in f:
        new_line = re.sub('[^a-zA-Z0-9_. ]+', ' ', line)
        n.write(new_line+'\n') 


input_data_file = "no_dup_ip.txt" 
dns_records = "all_exit_dns_records.txt" 

with open(input_data_file, 'r') as f, open(dns_records, 'w') as n:
    for line in f:
        if line.strip() == "0.0.0.0":
               pass
        else:
              name,alias,addresslist = lookup(line.strip())
              print name
	      print alias
	      print addresslist
	      alias =  nontype(alias)
 	      #print alias
              print  type(name),type(alias),type(addresslist)
	      n.write('{"Name": "' + name + '", "alias": "' + str(alias) + '", "addresslist": "' +str(addresslist) +'"}\n')
             
# n.write('{"Name": "' + name + '", "alias": "' + alias + '", "addresslist": "' +addresslist +'"}\n')
              #n.write(output)
         #            # sys.exit()
         #        # n.write(new_line+'\n')
#name,alias,addresslist = lookup('4.2.2.2')
