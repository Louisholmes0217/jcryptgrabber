import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

//import anbxj.Crypto_ByteArray;
//import anbxj.Crypto_SealedPair;
//import anbxj.*;

public class ObjCheck {

	public static void main(String... args) {
		

		try{
			System.out.println("Importing JAVA obj from file\n");
			FileInputStream fi = new FileInputStream(new File("../objout/obj_2_0_10.0.1.2,10.0.2.2.ser"));
			ObjectInputStream oi = new ObjectInputStream(fi);
			
			
			while(true) {
				Object x = oi.readObject();
				if(x == null) {
					break;
				}
				System.out.println(x.toString());
			}
			
			oi.close();
			fi.close();

		} catch (FileNotFoundException e) {
			System.out.println("File not found");
		} catch (IOException e) {
			System.out.println("End of file");
		} catch (ClassNotFoundException e) {
			System.out.println("Class not found");
		}
		}
}


