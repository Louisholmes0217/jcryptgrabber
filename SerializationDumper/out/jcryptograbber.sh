#! /bin/bash


rm streamoutput/*
rm objout/*
rm out.txt

if [ $1 == "" ]
then 
	exit 0
else
	:

tshark -r $1 -R "data and tcp" -2 -T fields -e tcp.stream -e ip.addr -e data > out.txt

python3 outparse.py

#python3 out2parse.py

for FILE in streamoutput/*;
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
