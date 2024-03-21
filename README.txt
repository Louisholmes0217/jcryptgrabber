*************
jcryptgrabber
*************
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
