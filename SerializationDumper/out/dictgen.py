

file = open("dictfile.txt", "w")

file.write("hextoascii {\n        ")
hexvals = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

counter = 0
for val in hexvals:
    for val2 in hexvals:
        #if val == "0":
        #    file.write('"'+val2+'"'+" : "+str(counter)+","+"\n        ")
        #    counter += 1
        
        #else:
        file.write('"'+val+val2+'"'+" : "+"b'\\x"+val+val2+"'"+","+"\n        ")
        counter += 1

file.write("}")
file.close()





#for i in range(0, 17):
#    for x in range(0,17):
#        if i == 0:
#            file.write(x+"\n        ")
