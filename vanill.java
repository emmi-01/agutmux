import java.io.*;

class x{
  public static void main(String[] args) {
     try{
         int x1 = 1;
         int x2 = 0;
         int res = x1/x2;
         System.out.println("Result came after division is: " + res);  
}
    
    catch(Throwable e){
         System.out.println("Failed to write to file due to the following error: " + e );
         e.printStackTrace();
    }

System.out.println("111111111111111111111111111");

  }

}
