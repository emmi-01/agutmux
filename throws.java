import java.io.*;

class x{
  public static void main(String[] args) throws IOException {
    FileWriter file = new FileWriter("./file.txt");
    file.write("Apg");
    file.close();
  }
}

