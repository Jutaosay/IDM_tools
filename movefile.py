# /etc/bin/env python3
# _*_ coding: utf-8 _*_

'movefile.py'

import os,shutil
#from user_defined import Chain

# demo function on master branch use default file source location
# Class Chain wil support user defined location by self input soon
# folder isinstance check and move under dev in dev branch

# source folder
fsource='/mnt/c/Users/Zen/Downloads' 
# destination folder
fdest='/mnt/e/Downloads'

def _movefile(a,b,*args,**kw):
    m=os.listdir(a)
    for x in m:
        x=os.path.join(a,x)
    #    print (x)
        try:
            shutil.move(x,b,copy_function=shutil.copy2)
            print("moving %s"%(x))
        except:                            # isinstance and raise exception under dev branch
            print("move fail")



if __name__=="__main__":
    _movefile(fsource,fdest)
    print ("move finished !")


