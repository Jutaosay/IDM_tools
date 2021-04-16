# /use/bin/enc python3
# _*_ coding:utf-8 _*_

'hashfile.py'

#

import hashlib,os

fsrc='/mnt/c/Users/Zen/Downloads'
#fsrc="/mnt/e/Downloads"
fhash='/mnt/e/Downloads/md5.txt'

def _hash_md5(a,b,*args,**kw):
    md5=hashlib.md5()
#   sha1=hashlib.sha1()        #sha1sum cost a lot of time, add that while use thread
    m=os.listdir(a)
    for x in m:
        x=os.path.join(x,a)
        print (x)
        with open(x,'rb') as f:
            y=md5.update(f.read())
            print(y.hexdigest())
#        try:
#        y=md5.update(x.encode('utf-8'))
#        print(y)
#        except:
#            print("hash filed")

if __name__=='__main__':
    _hash_md5(fsrc,fhash)
    print('hash finish')