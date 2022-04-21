#!/usr/bin/python3
import sys
import csv
import datetime

#fieldnames=["ts","srcip","dstip","srcprt","dstprt","bytes_sent","bytes_recv","total_bytes"]

#get unique values in lists
def unique(list1):
     
    # initialize a null list
    unique_list = []
     
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


#Read in exactly 1 argument
if len(sys.argv) == 2:
    log_file = sys.argv[1]
else:
    print('Error! - No Log File Specified!')
    exit()
try:
    #open csv file using the reader and cast to list
    with open(log_file,'r') as f:
        reader = csv.reader(f)
        data = list(reader)
except IOError:
    print("Error! - File Not Found!")
    exit()
hosed = []
c2 = []
ts = []
c2data=[]
tuples=()
#find the c2 address based on the dst ports used and add data to lists
for row in data:
    if row[4] == "1337" or row[4] == "1338" or row[4]=="1339" or row[4]=="1340":
        #print(row)
        hosed.append(row[1])
        c2.append(row[2])
        ts.append(row[0])

#get unique values in list
hosed = unique(hosed)
#sort IP address in acsending order
hosed = sorted(hosed, key=lambda ip: int(''.join(["%02X" % int(i) for i in ip.split('.')]), 16))

#get unique values in list
c2 = unique(c2)
#sort IP address in acsending order
c2 = sorted(c2, key=lambda ip: int(''.join(["%02X" % int(i) for i in ip.split('.')]), 16))

#Get total bytes transmitted to the C2 addresses with the C2 address in the tuple
for ip in c2:
    data_trans=0
    for row in data:
        if row[2] == ip:
            data_trans+=int(row[5])
    c2data.append((ip,data_trans))

#sort based on the second element of the tuple in decending order 
c2data.sort(key=lambda x: x[1],reverse=bool(True))

#sort unix time stamp list in acsending order giving us the earliest time
ts.sort()
#format time to standard time format
date = datetime.datetime.utcfromtimestamp(int(ts[0])).strftime('%Y-%b-%d %X UTC')

print('Source File: '+log_file)
print('Systems Infected: '+str(len(hosed)))
print('Infected System IPs: ',end='')
print(hosed)
print('C2 Servers: '+str(len(c2)))
print('C2 Server IPs:',end='')
print(c2)
print('First C2 Connection: '+date)
print('C2 Data Totals: ',end='')
print(c2data)