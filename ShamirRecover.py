from __future__ import absolute_import, division, print_function
from builtins import *
import TSS
from tkinter import *
import tkinter.messagebox
import ShamirMenu
from binascii import unhexlify
import ntpath
import os
from io import open
import glob
import time





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



class ShamirR():

    def __init__(self, master):
        self.shares     = []
        self.key        = StringVar()
        self.sourceSpec   = StringVar()
        self.destSpec = StringVar()
        self.recShareSize  = IntVar()
        self.recThreshold  = IntVar()


        self.master = master
        self.master.geometry('400x200+100+80')
        self.master.title('Secret Recovery')

        self.lRec1 = Label(self.master, text="Source Directory").grid(row=1, column=0, sticky=E)
        self.lRec2 = Label(self.master, text="Destination Directory").grid(row=2, column=0, sticky=E)

        self.entryRec1 = Entry(self.master, textvariable=self.sourceSpec, bd=2).grid(row=1, column=1)
        self.entryRec2 = Entry(self.master, textvariable=self.destSpec, bd=2).grid(row=2, column=1)

        self.myButRec1 = Button(self.master, text="Submit", width=7, command=self.submitRecovery).grid(row=4, column=1, sticky=W)
        self.myButRec2 = Button(self.master, text="Back", width=8, command=self.seeMainMenu).grid(row=4, column=1,sticky=E)


    def submitRecovery(self):
            nSourceSpec = self.sourceSpec.get()
            nDestSpec = self.destSpec.get()


            d = ntpath.abspath(ntpath.join('C:\\', nSourceSpec))
            if not os.path.exists(d):
                print('Directory does not exist')

            else:
                path = d
                rout = '*.*'
                files = glob.glob(os.path.join(path, rout))
                list_of_files = glob.iglob(os.path.join('./*.bin'))

                shares = []
                for ful, file in [(ful, file) for ful in list_of_files for file in files]:
                    with open(ful, 'rb+') as d:
                        dReader = d.read().splitlines()


                    for share in dReader:
                        f = (share.split(':')[1].lstrip(path))
                        fils = (share.split(':')[2])
                        fil = file.lstrip(path)

                        if f == fil:
                            try:
                                deal = eval(fils)
                                deal = unhexlify(deal)
                                shares.append(deal)
                            except Exception:
                                print('%s share in %s could not be read' % (fil, ful))


                start = time.time()
                key = TSS.reconstruct_secret(shares, strict_mode=True)
                key = str(key)
                end = time.time()
                processtime = end - start
                print('Time taken to recover secret:%f' % processtime)
                print('Writing files to %s directory' % nDestSpec)

                try:
                    dirname = nDestSpec
                    os.mkdir(dirname)
                    os.chdir(dirname)
                except OSError:
                    pass

                for file in files:
                    fil = file.lstrip(path)

                    with open(fil, 'ab+') as foo:
                        foo.write(key)

                tkinter.messagebox.showinfo('Status Message', 'Your Secret is successfully recovered, BACK to Main Menu')



    def seeMainMenu(self):
        self.master.destroy()
        ShamirMenu.main()



def main():
    root = Tk()
    myGUIRec = ShamirR(root)
    root.mainloop()


if __name__ == '__main__':
    main()
