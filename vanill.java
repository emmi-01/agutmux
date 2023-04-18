import java.io.*;

class x{
  public static void main(String[] args) {
     try{
           FileWriter file = new FileWriter("./file.txt");
           file.write("Apg");
           file.close();
    }
    catch(IOException e){
       //Handle exception here
    }
  }
}
