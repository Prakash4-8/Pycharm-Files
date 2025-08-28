import java.io.*;

public class StringManipulation {
    public static void main(String[] args)throws IOException {
       FileInputStream sourceStream = null;
       FileOutputStream destStream = null;
       try {
        sourceStream = new FileInputStream("LinearSearch.java");
        destStream = new FileOutputStream("LinearTargetSearch.java");
        int temp;
        while ((temp = sourceStream.read())!= -1 ) {
            destStream.write((byte)temp);
        }
       }
       finally{
        if(sourceStream != null)
        sourceStream.close();
        if(destStream != null)
        destStream.close();
       }
       
    }
}
