#!/usr/bin/python3
import os
import sqlite3
import sys
import pysqlite3

#Read in exactly 1 argument
if len(sys.argv) == 2:
    history_file = sys.argv[1]
else:
    print('Error! - No History File Specified!')
    exit()

try:
    s = sqlite3.connect(history_file)
except OSError:
    print('Error! - File Not Found!')
    exit()

s.close()