*************
jcryptgrabber
*************
Preamble:
This tool was developed as part of a final year project for my University 
course, Cyber Security and Networks. I was given the task to extract 
cryptographic elelments from a packet capture file in the form of serialized
Java objects. My solution was a combination of existing tools, and a simple
parser that would detect and reconstruct Java elements within a Pcap file.

Author:	Louis Holmes

Requirements/Dependancies: 
	- Java,
	- Python3,
	- Ecliplse AnBx ide plugin (for objcheck only)

Installation: No installation needed, 
just ensure all dependancies are installed

Instructions:
Call the program with "./jcryptgrabber [pathtopcapfile] [identifier]"
[pathtopcapfile] is the path to the pcap file you wish to extract
Java objects from. It must contain at least 1 Java object with
some content in order for the tool to function.

the [identifier] argument is optional and can be ommited, adding
an argument here will append the string you set to the start of any
file related to the specific PCAP file. This can be used to seperate
between different protocols and PCAP files in the out folders.

A "clear.sh" program has been included to conveniently empty any previously
extracted content in the out.txt file, objout/ and streamout/ folders.
Simply run this with "./clear.sh" before beginning your project.

An "ObjCheck.jar" tool has also been included for reading in the java objects.
Simply change the filepath in the .java file to your chosen .ser file and
compile/run to check the validity of the objects and get its values.

Input/Output:
The tool takes the path to a pcap file as an input. The output
is in the form of .txt files and .ser files. The .txt files are an
ascii representation of any discovered Java objects in hex. Each object
is saved in its own file in the order the object came accross the network.
The .ser files are a reconstruction of the original Java object in litteral
binary, meaning these files can be read into a Java program or deserialized
by another analysis tool.
The filenames for each file is as follows:
[optional identifier_][TCP stream identifier]_[source address],[destination address].txt/ser

The .txt files are saved in "streamout/",
the .ser files are saved in "objout/".

example (no identifier):
	- "./jcryptgrabber Fresh_From_A_DY.pcap"
	output: streamout/1_0_10.1.1.0,10.1.2.0.txt
					  2_0_10.1.2.0,10.1.1.0.txt

			objout/1_0_10.1.1.0,10.1.2.0.ser
				   2_0_10.1.2.0,10.1.1.0.txt

example (no identifier):
	- "./jcryptgrabber Fresh_From_A_DY.pcap FFADY"
		output: streamout/FFADY_1_0_10.1.1.0,10.1.2.0.txt
					  FFADY_2_0_10.1.2.0,10.1.1.0.txt

				objout/FFADY_1_0_10.1.1.0,10.1.2.0.ser
				   	  FFADY_2_0_10.1.2.0,10.1.1.0.ser
