#! /bin/bash

rm out.txt
datatype=$2
	
if [ $1 == "" ]
then 
	exit 0
else
	:

tshark -r $1 -R "data and tcp" -2 -T fields -e tcp.stream -e ip.addr -e data > out.txt

python3 outparse.py $datatype

rm out.txt # Remove this line for debugging purposes when testing 1 pcap at a time

for FILE in streamout/${datatype}*;
do
	if [[ $(cat $FILE) == *"aced"* ]]; then
		echo $FILE
		java -jar SerializationDumper/SerializationDumper.jar $(cat $FILE)
		echo ""
		echo "......................................."
		echo ""
	else
		:
	fi	
done
fi
exit 0
