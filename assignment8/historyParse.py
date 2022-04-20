#!/usr/bin/python3
import os
import sys
import sqlite3
import datetime

#Read in exactly 1 argument
if len(sys.argv) == 2:
    history_file = sys.argv[1]
else:
    print('Error! - No History File Specified!')
    exit()
try:
    f = open(history_file)
except IOError:
    print("Error! - File Not Found!")
    exit()
try:
    s = sqlite3.connect(history_file)
except OSError:
    print('Error! - File Not Found!')
    exit()

cur = s.cursor()

print('Source File: '+history_file)

cur.execute('SELECT COUNT(*) FROM "main"."downloads"')
print('Total Downloads: '+str(cur.fetchone()[0]))

cur.execute('SELECT * FROM "main"."downloads";')
downloads = cur.fetchall()
print(downloads)

cur.execute('SELECT COUNT (DISTINCT term) FROM "main"."keyword_search_terms"')
print('Unique Search Terms: '+ str(cur.fetchone()[0]))

cur.execute('SELECT term FROM "main"."keyword_search_terms"  ORDER BY "url_id" DESC LIMIT 1;')
print('Most Recent Search: '+cur.fetchone()[0])

cur.execute('SELECT url_id FROM "main"."keyword_search_terms"  ORDER BY "url_id" DESC LIMIT 1;')
url_id = cur.fetchone()[0]
cur.execute('SELECT last_visit_time from "main"."urls" WHERE id = '+str(url_id)+';')
search_timestamp = cur.fetchone()[0]
search_time = (datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=search_timestamp))
print("Most Recent Search Date/Time: "+search_time.strftime('%Y-%b-%d %X'))
s.close()