if len(sys.argv) > 1:
    datatype = sys.argv[1]+"_"
else:
    datatype = ""

f = open("out.txt", "r")



class pcapObj:
    def __init__(self, stream, data):
        self.stream = stream
        self.data = data

class validStream :
    def __init__(self, streamIndex, addressPair):
        self.streamIndex = streamIndex
        self.addressPair = addressPair

valid_streams = [] 
objs = []
last_identifier = ""

for line in f.readlines():
    line = line.strip()
    line = line.split("\t")
    
    if line[2].startswith("aced0005"):
        valid_stream = (line[0]+"_"+line[1])
        valid_streams.append(valid_stream)
        continue
    
    stream = line[0]+"_"+line[1]
    if stream in valid_streams:

        if stream != last_identifier:
            obj = pcapObj(stream, "aced0005"+line[2])
            objs.append(obj)
        else:
            (objs[len(objs)-1]).data += line[2]

        last_identifier = stream

f.close()

for i in range(len(objs)):
    obj = objs[i]
    f = open("objout/"+datatype+str(i+1)+"_"+obj.stream+".ser", "wb")
    data = bytes.fromhex(obj.data)
    f.write(data)

for i in range(len(objs)):
    obj = objs[i]
    f = open("streamout/"+datatype+str(i+1)+"_"+obj.stream+".txt", "w")
    data = obj.data
    f.write(data)
