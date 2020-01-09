import glob
import os


def splitFile():
    path = r'c:\\Tests\Crypto101.pdf'
    paths = r'c:\\Cat'


    with open(path, 'rb+') as fileRead:
        data = fileRead.read() # read the entire content of the file

    bytes = len(data)
    max_size = int((bytes + 1024)/1024)
    ext = 'Cryto101.pdf'

    os.mkdir(paths)
    os.chdir(paths)

    fileNames = []
    d = 1
    for i in range(0, bytes+1, max_size):
        fn1 = 'file%s' % i + '.%03d' %d
        fileNames.append(fn1)


        f = open(fn1, 'wb')
        f.write(data[i:i+max_size])
        d += 1
        f.close()




    dataList = []
    for fn in fileNames:
        f2 = open(fn, 'rb')
        dataList.append(f2.read())
        f2.close()

    f3 = open(ext, 'wb')
    for dats in dataList:
        f3.write(dats)
    f3.close()


splitFile()

