import binascii
import dictfile

FILE = open("out.txt", "r")
mydict = {

         }


counter = 0

for line in FILE.readlines():
    linearray=line.split("\t")
    currentstream = linearray[0]+"_"+linearray[1]
    if currentstream in mydict:
        mydict[currentstream] = mydict[currentstream]+linearray[2].strip()
    else:
        mydict[currentstream] = linearray[2].strip()

FILE.close()

for i in mydict:
    FILE = open("streamoutput/"+str(counter)+"_"+i+".txt", "w")
    SER_FILE = open("objout/obj_"+str(counter)+"_"+i+".ser", "wb")
    FILE.write(mydict[i])
#    raw_bytes = (bin(int.from_bytes(binascii.unhexlify(mydict[i]), byteorder='big')))
#    SER_FILE.write(raw_bytes)
#    for c in mydict[i]:
#        SER_FILE.write(asciitohex[c])
    tmpcount = 0
    currentdata = mydict[i].strip()
    while tmpcount < len(currentdata):
        currentbyte = currentdata[tmpcount]
        currentbyte = currentbyte+currentdata[tmpcount + 1]
        binarybyte = dictfile.asciitohex[currentbyte]
        SER_FILE.write(binarybyte)
        tmpcount += 2


    FILE.close()
    SER_FILE.close()
    counter += 1

