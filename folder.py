import os
import hashlib
import sys

"""
cwd = os.getcwd()
print("Current working directory:", cwd)

filelist = os.listdir()
for f in filelist:
    print(f)
"""
def GhiFile(noiDung):
    noiDung=str(noiDung)
    dir="hash.txt"
    file=open(dir,"a")
    file.write(noiDung)
    file.write("\n")
    file.close()

def HashNoiDung(dir):
    """"lay ham bam cua anoi dung trong file"""
    file=open(dir)
    data=file.read()
    hashCode=hashlib.sha256(data.encode())
    hashCode=hashCode.hexdigest()
    file.close()
    return str(hashCode)


def Hash(dir):
    """"lay ham bam của ten"""
    hashCode=hashlib.sha256(str(dir).encode())
    hashCode=hashCode.hexdigest()
    return str(hashCode)


#filelistt = os.walk("C:/Users/Admin/Desktop/hinh anh tttn")
#for f in filelistt:
#    print(f)

#print("\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
#for (root,dirs,files) in os.walk("C:/Users/Admin/Desktop/hinh anh tttn", topdown=True):
#        print (root)
#        print (dirs)
#        print (files)
#        print ('--------------------------------')

list=[]
for (root,dirs,files) in os.walk("C:/Users/Admin/Desktop/hinh anh tttn"):
    
    """
    #print (root)
    #hash root
    tmp=Hash(root)
    GhiFile(tmp)
    #print (dirs)
    #hash cac folder
    for i in dirs:
        tmp=Hash(root+"//"+i)
        GhiFile(tmp)
    #print (files)
    #hash noi dung cua file
    for i in files:
        #dir=root+"/"+i
        tmp=HashNoiDung(root+"//"+i)
        GhiFile(tmp)
    """    
    list.append(root)
    GhiFile(Hash(root))
    print(root)
    for i in dirs:
        list.append(os.path.join(root,i))
        print(os.path.join(root,i))
        tmpp=os.path.join(root,i)
        GhiFile(Hash(tmpp))
    for i in files:
        list.append(os.path.join(root,i))
        print(os.path.join(root,i))
        #GhiFile(HashNoiDung(os.path.join(root,i)))
        tmpp=os.path.join(root,i)
        GhiFile(Hash(tmpp))
    print ('--------------------------------')



print(list)
tong=0
for i in list:
    print(os.path.exists(i))
    
    tong=tong+1
    
print("tong la:",tong)
