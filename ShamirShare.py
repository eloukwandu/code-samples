from __future__ import absolute_import, division, print_function
from builtins import *
import os
from binascii import hexlify
import os.path
import time
import glob
import TSS
from tkinter import *
import tkinter.messagebox
import ShamirMenu
import ntpath
import chardet
from io import open




def time_usage(func):
    def wrapper(*args, **kwargs):
        beg_ts = time.time()
        func(*args, **kwargs)
        end_ts = time.time()
        print("elapsed time: %f" % (end_ts - beg_ts))
    return wrapper

@time_usage
def test():
    for i in range(0, 10000000):
        pass

if __name__ == "__main__":
    test()


class ShamirS():


    def __init__(self, master):
        self.secretData = StringVar()
        self.shareSize  = IntVar()
        self.threshold  = IntVar()
        self.result     = StringVar()
        self.fileName   = StringVar()

        self.master = master
        self.master.geometry('400x200+100+80')
        self.master.title('Secret Sharing')

        self.lShare1 = Label(self.master, text="Share Size(n is int, 5)").grid(row=1, column=0, sticky=E)
        self.lShare2 = Label(self.master, text="Threshold(k is 3 less than n)").grid(row=2, column=0, sticky=E)
        self.lShare3 = Label(self.master, text="Folder").grid(row=3, column=0, sticky=E)
        self.lShare4 = Label(self.master, text="Identifier (a-z, 0-9)").grid(row=4, column=0, sticky=E)

        self.entryShare1 = Entry(self.master, textvariable=self.shareSize, bd=2).grid(row=1, column=1)
        self.entryShare2 = Entry(self.master, textvariable=self.threshold, bd=2).grid(row=2, column=1)
        self.entryShare3 = Entry(self.master, textvariable=self.secretData, bd=2).grid(row=3, column=1)
        self.entryShare4 = Entry(self.master, textvariable=self.fileName, bd=2).grid(row=4, column=1)


        self.myButton1 = Button(self.master, text="Submit", width=7, command=self.submitSecret).grid(row=5, column=1,sticky=W)
        self.myButton2 = Button(self.master, text="Back", width=8, command=self.gotoMainMenu).grid(row=5, column=1,sticky=E)


    def submitSecret(self):
        nShares     =   self.shareSize.get()
        nThreshold  =   self.threshold.get()
        f           =   self.secretData.get()
        iden        =   self.fileName.get()

        d = ntpath.abspath(ntpath.join('C:\\', f))
        if not os.path.exists(d):
            print('Directory does not exist')

        else:

            path = d
            rout = '*.*'
            route = glob.iglob(os.path.join(path, rout))

            for infile in route:
                if infile[0] == '.' or infile == '*._*':
                    continue


                with open(infile, 'rb+') as infilesecret:
                    secretRead = infilesecret.read()

                    secret = secretRead

                    res = chardet.detect(secret)
                    chrenc = res['encoding']
                    print(chrenc)

                    infilelen = len(infile)
                    infilesize = os.path.getsize(infile)

                    print('current file being read is:  %s' % infile.lstrip(path))
                    print('created: %s' % time.ctime(os.path.getmtime(infile)))
                    print('last modified: %s' % time.ctime(os.path.getmtime(infile)))
                    print('length: %d' % infilelen)
                    print('size: %d' % infilesize)
                    print()

                    id = iden.encode('utf-8', errors='strict')
                    key = secret
                    TSS.Hash.SHA256 = 2

                    start = time.time()
                    print('%s: Share is being created' % infile)
                    self.result = TSS.share_secret(nThreshold, nShares, key, id, TSS.Hash.SHA256)
                    results = self.result
                    print(results)
                    end = time.time()
                    endtime = end - start
                    print('Time taken to create shares:%f' % endtime)

                    print((infile) + ':')
                    print("Share 1:%s" % hexlify(results[0]))
                    print("Share 2:%s" % hexlify(results[1]))
                    print("Share 3:%s" % hexlify(results[2]))
                    print("Share 4:%s" % hexlify(results[3]))
                    print("Share 5:%s" % hexlify(results[4]))

                    r0 = hexlify(results[0])
                    r1 = hexlify(results[1])
                    r2 = hexlify(results[2])
                    r3 = hexlify(results[3])
                    r4 = hexlify(results[4])


                    print('Wait....writing to file')
                    print('Done!!!')


                    with open('shahex0.bin', 'ab+') as d0:
                        d0.write(str(infile) + ':')
                        d0.write(repr(bytes(r0)))
                        d0.write('\n')

                    with open('shahex1.bin', 'ab+') as d1:
                        d1.write(str(infile) + ':')
                        d1.write(repr(bytes(r1)))
                        d1.write('\n')

                    with open('shahex2.bin', 'ab+') as d2:
                        d2.write(str(infile) + ':')
                        d2.write(repr(bytes(r2)))
                        d2.write('\n')

                    with open('shahex3.bin', 'ab+') as d3:
                        d3.write(str(infile) + ':')
                        d3.write(repr(bytes(r3)))
                        d3.write('\n')

                    with open('shahex4.bin', 'ab+') as d4:
                        d4.write(str(infile) + ':')
                        d4.write(repr(bytes(r4)))
                        d4.write('\n')

                    tkinter.messagebox.showinfo('Status Message', 'Shares Successfully Created, BACK to Main Menu')


    def gotoMainMenu(self):
        self.master.destroy()
        ShamirMenu.main()


def main():
    root = Tk()
    myGUIShare = ShamirS(root)
    root.mainloop()

if __name__ == '__main__':
    main()

