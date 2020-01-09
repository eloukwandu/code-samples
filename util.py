'''
Utilities for testing file concatenation in Python.
'''

import subprocess,time

def timed(f):
    def func(*args):
        start = time.time()
        ret = f(*args)
        took = time.time() - start
        print("%s took %f" % (f.__name__,took))
        return ret
    return func

def yield_json(lines):
    '''Iterates over a file yeilding JSON objects.  Expects the files
    to be indented, such that root objects end '}' at the first index
    of the line.
    '''
    store = []
    for ln in lines:
        if ln and ln[0] == '}': # End of object
            store.append('}')
            ret = store
            store = [ln[1:]]
            yield ''.join(ret)
        else:
            store.append(ln)

use_clean_cache=False
def clear_cache():
    '''Attempts to clear disk caches on Linux - must be run as root'''
    if use_clean_cache:
        subprocess.call("sync; echo 3 > /proc/sys/vm/drop_caches", shell=True)