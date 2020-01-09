import os
import glob
import shutil
import sqlite3
import hashlib
import uuid
import datetime
import time


conn = sqlite3.connect('catShaWork.db')
c = conn.cursor()
now = datetime.datetime.now()


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
        fil = os.path.basename(infile)
        a = uuid.uuid4()
        infilesize = os.path.getsize(infile)
        c.execute("INSERT INTO workToPlot(datetime, id, uuid, filename, filesize) VALUES (?, ?, ?, ?, ?)", (DATE, str(id), str(a), fil, infilesize))
        conn.commit()


def splitjoinFile():
    c.execute('SELECT * from workToPlot')
    data = c.fetchall()

    path = r'c:\\test'
    paths = r'c:\\CatFiles'
    nameDir = r'C:\\Users\Elochukwu Ukwandu\PycharmProjects\Dec08pract'
    rout = '*.*'
    route = glob.iglob(os.path.join(path, rout))

    try:
        os.mkdir(paths)
    except OSError:
        pass


    for infile, row in [(infile, row) for infile in route for row in data]:
        if infile[0] == '.' or infile == '*._*' or infile == '~*.*':
            os.remove(infile)
            continue

        ext = os.path.basename(infile)
        max_size = 102400
        infilesize = os.path.getsize(infile)
        fileName = (os.path.splitext(ext)[0])

        with open(infile, 'rb+') as fileRead:
            data = fileRead.read()


        bytes = len(data)
        noOfChunks = bytes / max_size

        if (bytes % max_size):
            noOfChunks += 1

        os.chdir(paths)
        chunkNames = []
        for i in range(0, bytes + 1, max_size):
            fn1 = "chunk%s" % i
            chunkNames.append(fn1)

            f = open(fn1, 'wb')
            f.write(data[i:i + max_size])
            f.close()




        dataList = []
        for i in range(0, noOfChunks, 1):
            chunkNum = i * max_size

            chunkName = fileName + '%s' % chunkNum

            f = open(chunkName, 'rb')
            dataList.append(f.read())
            f.close()

            os.chdir(nameDir)
            f = open(fileName, 'wb')
            for data in dataList:
                f.write(data)
                f.close()


create_table()
self_data_entry()
splitjoinFile()
