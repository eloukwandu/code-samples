import os
import os.path
import time
import glob
from io import open
import sqlite3
from Crypto.Cipher import AES
import hashlib
import base64
from binascii import unhexlify
import TSS



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


conn = sqlite3.connect('phdwork.db')
c = conn.cursor()


class ReadBoth(object):
    def read_from_both(self):
        c. execute('SELECT * from workToPlot')
        data = c.fetchall()

        list_of_files = glob.iglob(os.path.join('./G*.txt'))

        shares = []
        for ful, row in [(ful, row) for ful in list_of_files for row in data]:

            with open(ful, 'r+') as d:
                dReader = d.read().splitlines()

            for share in dReader:
                b = share.split(':')[3]
                ch = share.split(':')[4]
                g = row[2]
                g_enc = g.encode('utf-8', 'strict')
                g_hash = hashlib.sha256(g_enc).hexdigest()

                fil = row[3].lstrip()

                if str(b) == str(g_hash):
                    try:
                        deal = eval(ch)
                        deals = unhexlify(deal)
                        shares.append(deals)
                    except Exception:
                        print('%s share in %s could not be read' % (fil, ful))

        start = time.time()
        key = TSS.reconstruct_secret(shares, strict_mode=False)
        key = base64.a85decode(key)
        end = time.time()
        processtime = end - start
        print('Time taken to recover secret:%f' % processtime)
        return key



    def decryptfiles(self, key):
        c.execute('SELECT * from workToPlot')
        data = c.fetchall()

        unpad = lambda s: s[:-ord(s[len(s) - 1:])]

        path = r"c:\\encryptedfiles"
        o_files = '*.enc'


        list_of_enc_files = glob.iglob(os.path.join(path, o_files))

        print()
        print('File decryption in progress, please provide the details below')
        print('Destination folder name:')
        nameDir = input()

        print("First name:")
        fname = input()

        print("Othername:")
        oname = input()

        print('Surname:')
        sname = input()

        print('Initial password')
        pasw = input()

        password = fname + oname + sname + pasw
        password = password.encode('utf-8', 'strict')

        id = hashlib.sha256(password).hexdigest()

        try:
            os.mkdir(nameDir)
        except OSError:
            pass

        print('Writing files to %s directory' % nameDir)

        for file in list_of_enc_files:
            start = time.time()
            cipher = AES.new(key, AES.MODE_ECB)


            ext = os.path.basename(file)
            filename = (os.path.splitext(ext)[0])
            filesize = os.path.getsize(file)



            with open(file, 'rb') as file_dec:
                dec_file = file_dec.read()
                dec = cipher.decrypt(dec_file)
                dec = unpad(dec).decode('latin_1', 'strict')
                end = time.time()
                processtime = end - start
                print('Time taken to decrypt %s, of size %d is %f' % (file, filesize, processtime))


                try:
                    os.chdir(nameDir)
                except OSError:
                    pass

                with open(filename, 'ab+') as foo:
                    foo.write(str.encode(dec, 'latin_1', 'strict'))

        print('Successfully written to the directory!!!!')


ss = ReadBoth()
key = ss.read_from_both()

ss.decryptfiles(key)


c.close()
conn.close()