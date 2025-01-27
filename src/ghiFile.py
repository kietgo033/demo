import random
 

file1=open("solieu.txt","w",10)
tmp=0
for i in range(10):
    for j in range(5):
        val = random.randint(0, 100)
        while(tmp==val):
            val = random.randint(0, 100)
        str_val = str(val)
        file1.write(str_val)
        file1.write(" ")
        tmp=val
    file1.write("\n")
file1.close()
