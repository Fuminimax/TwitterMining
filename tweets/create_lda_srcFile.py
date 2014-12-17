'''
Created on 2014/12/15

@author: root
'''
# -*- coding: utf-8 -*-

import mysql.connector
import sys
from pprint import pprint

mysqlcon = mysql.connector.connect(host='192.168.120.28',
                                    port = 3306,
                                    db = 'TwitterMining',
                                    user = 'fumio',
                                    passwd = 'fumio1226',
                                    charset = 'utf8')
curs = mysqlcon.cursor()

rows = curs.execute("SELECT document_id, words from lda_document_word")
records = curs.fetchall()

mysqlcon.commit()

fp = open('./data/newdata.dat', 'a')

fp.write(str(len(records)) + '\n')

for record in records:

    fp.write(record[1].encode('utf-8') + '\n')
    
fp.close()