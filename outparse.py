import binascii
import sys

# Opening file generated by tshark
FILE = open("out.txt", "r")

# Checking for included filetype
if len(sys.argv) > 1:
    datatype = sys.argv[1]+"_"
else:
    datatype = ""

# Dict used when collating data from the out.txt file, 
# the key is the stream value, and the data is the tcp data
mydict = {

         }

# Concatinating the data from each packet into a single stream
counter = 1
for line in FILE.readlines():
    linearray=line.split("\t")
    currentstream = linearray[0]+"_"+linearray[1]
    if currentstream in mydict:
        mydict[currentstream] = mydict[currentstream]+linearray[2].strip()
        
    else:
        mydict[currentstream] = linearray[2].strip()

FILE.close()

for i in mydict:
    
    FILE = open("streamout/"+(datatype)+str(counter)+"_"+i+".txt", "w")
    SER_FILE = open("objout/obj_"+(datatype)+str(counter)+"_"+i+".ser", "wb")
    FILE.write(mydict[i])
    currentdata = mydict[i].strip()
    data = bytes.fromhex(currentdata)
    SER_FILE.write(data)


    FILE.close()
    SER_FILE.close()
    counter += 1

