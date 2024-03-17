#! /bin/bash

datatype=$2
echo "Clear folders?"
read answer

if [[ answer == "y" ]]
then
	rm out.txt
	rm objout/*
	rm stream/*
else
	:
fi

if [[ -f streamout/${datatype}* ]]
then
	rm streamout/${datatype}*
else
	:
fi

if [[ -f objout/obj_${datatype}* ]]
then
	rm objout/obj_${datatype}*
else
	:
fi
	
rm out.txt

if [ $1 == "" ]
then 
	exit 0
else
	:

tshark -r $1 -R "data and tcp" -2 -T fields -e tcp.stream -e ip.addr -e data > out.txt

python3 outparse.py $datatype

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
