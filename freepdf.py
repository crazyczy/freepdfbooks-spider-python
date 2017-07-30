# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 14:56:39 2017

@author: crazyczy
"""

import os
import requests
import re
import time
import sqlite3


url = 'http://freepdf-books.com/download/?file='

if not os.path.exists('pdfs'):
    os.mkdir('pdfs')

if not os.path.exists('pdfimages'):
    os.mkdir('pdfimages')

header = {
    'Upgrade-Insecure-Requests':'1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.3\
    6 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    'Cookie': ''  # You need to fill in the cookie.
}

if __name__ == '__main__':
    conn = sqlite3.connect('pdfinfo.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS "main"."info";')
    cursor.execute('CREATE TABLE "info" ("id" INTEGER NOT NULL,"filename" TEXT (100) NOT NULL,"pages" INTEGER NOT NULL,"filesize" TEXT(10) NOT NULL,"download" INTEGER NOT NULL,PRIMARY KEY ("id" ASC));')
    for id in range(1, 10000):
        try:
            req = requests.get(url + str(id), headers = header, timeout = None)
            filesize = re.search(r'<span class="doc-meta-download">Filesize (.*)</span>', req.text).group(1)

            if filesize != '0 bytes':
                turl = re.search(r'window.location.replace.*;', req.text).group(0).split('"')[1]
                filename = turl.split('/')[-1].replace(' - FreePdfBook','')
                pages = re.search(r'<span class="doc-meta-download">Pages (.*)</span>', req.text).group(1)
                downloaded = re.search(r'<span class="doc-meta-download">Downloaded (.*) times</span>', req.text).group(1)

                pdf = requests.get(turl, headers = header)
                img = requests.get('http://freepdf-books.com/doc-images/'+str(id)+'.png', timeout = None)
                with open('pdfimages/' + str(id) + '.png', 'wb') as code1:
                    code1.write(img.content)
                with open('pdfs/' + filename, 'wb') as code2:
                    code2.write(pdf.content)

                cursor.execute('insert into info (id, filename, pages, filesize, download) values ('+str(id)+', \''+str(filename)+'\','+str(pages)+',\''+str(filesize)+'\','+str(downloaded)+');')
                conn.commit()
                print id, pages, filesize, downloaded, filename
        except:
            time.sleep(60)
    cursor.close()
    conn.close()
