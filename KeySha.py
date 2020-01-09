import os
import os.path
import uuid
import time
import glob
from io import open
import sqlite3
import datetime
from Crypto.Cipher import AES
import shutil
import hashlib
import base64
from binascii import hexlify
import TSS



now = datetime.datetime.now()


conn = sqlite3.connect('phdwork.db')
c = conn.cursor()

def create_table():
    c .execute('CREATE TABLE IF NOT EXISTS workToPlot (datetime DATE, id TEXT, uuid TEXT, filename TEXT, filesize INT)')


def self_data_entry():
    print("First name:")
    fname = input()

    print("Othername:")
    oname = input()

    print('Surname:')
    sname = input()

    print('Preferred password')
    pasw = input()

    password = fname + oname + sname + pasw
    password = password.encode('utf-8', 'strict')

    DATE = now.strftime("%Y-%m-%d %H:%M")

    path = r'c:\\test'
    rout = '*.*'
    route = glob.iglob(os.path.join(path, rout))


    for id, infile in enumerate(route):

        id = hashlib.sha256(password).hexdigest()

        #fil = infile.lstrip(path)
        fil = os.path.basename(infile)
        a = uuid.uuid4()
        infilesize = os.path.getsize(infile)
        c.execute("INSERT INTO workToPlot(datetime, id, uuid, filename, filesize) VALUES (?, ?, ?, ?, ?)", (DATE, str(id), str(a), fil, infilesize))
        conn.commit()

def encrypt_read_db():
    BS = 16
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()

    c. execute('SELECT * from workToPlot')
    data = c.fetchall()

    sh = 5
    th = 3

    nameDir = r"c:\\encryptedfiles"
    try:
        os.mkdir(nameDir)
    except OSError:
        pass

    path = r'c:\\test'
    rout = '*.*'
    route = glob.iglob(os.path.join(path, rout))

    secret = os.urandom(BS)


    for infile in route:
        files = infile.lstrip(path)

        if infile[0] == '.' or infile == '*._*':
            continue


        cipher = AES.new(secret, AES.MODE_ECB)

        with open(infile, 'rb') as secretRead:
            file_to_enc = secretRead.read()


        raw = pad(file_to_enc)
        enc = cipher.encrypt(raw)

        file_enc = infile + '.enc'
        iden = 'phdworks'

        with open(file_enc, 'ab') as fw:
            fw.write(enc)


        infilelen = len(infile)
        infilesize = os.path.getsize(infile)

        print('current file being read is:  %s' % infile.lstrip(path))
        print('created: %s' % time.ctime(os.path.getmtime(infile)))
        print('last modified: %s' % time.ctime(os.path.getmtime(infile)))
        print('length: %d' % infilelen)
        print('size: %d' % infilesize)
        print()

        nshares = int(sh)
        nthreshold = int(th)
        id = str.encode(iden, encoding='latin_1', errors='strict')

        key = base64.a85encode(secret)

        start = time.time()
        print('%s: Share is being created' % infile)
        results = TSS.share_secret(nthreshold, nshares, key, id, TSS.Hash.SHA256)
        end = time.time()
        endtime = end - start
        print('Time taken to create shares:%f' % endtime)


        shutil.move(file_enc, nameDir)
        os.remove(infile)

        for row in data:
            if files == row[3]:
                idx = row[2]
                idx = idx.encode('utf-8', 'strict')
                a0 = hashlib.sha256(idx).hexdigest()
                b0 = (now.strftime("%Y-%m-%d %H:%M:"))

                c0 = hexlify(results[0])
                c1 = hexlify(results[1])
                c2 = hexlify(results[2])
                c3 = hexlify(results[3])
                c4 = hexlify(results[4])


                with open("GUID0.txt", 'a+') as fstore0:
                    fstore0.write(b0 + ':')
                    fstore0.write(a0 + ':')
                    fstore0.write(str(c0))
                    fstore0.write('\n')

                with open("GUID1.txt", 'a+') as fstore1:
                    fstore1.write(b0 + ':')
                    fstore1.write(a0 + ':')
                    fstore1.write(str(c1))
                    fstore1.write('\n')

                with open("GUID2.txt", 'a+') as fstore2:
                    fstore2.write(b0 + ':')
                    fstore2.write(a0 + ':')
                    fstore2.write(str(c2))
                    fstore2.write('\n')

                with open("GUID3.txt", 'a+') as fstore3:
                    fstore3.write(b0 + ':')
                    fstore3.write(a0 + ':')
                    fstore3.write(str(c3))
                    fstore3.write('\n')

                with open("GUID4.txt", 'a+') as fstore4:
                    fstore4.write(b0 + ':')
                    fstore4.write(a0 + ':')
                    fstore4.write(str(c4))
                    fstore4.write('\n')


def main():
    create_table()
    self_data_entry()
    encrypt_read_db()

if __name__=="__main__":
    main()


c.close()
conn.close()