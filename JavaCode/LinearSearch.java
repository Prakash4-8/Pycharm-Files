import java.util.*;
public class LinearSearch
{
    public static void main(String[] args) {
        int arr1[] = {10,23,03,10};
        int val = 3;
        boolean falg = false;
        int i =0;
        for (; i < arr1.length;i++){
            if (arr1[i] == val){
                falg = true;
                break;
            }            
        }
        if(falg == true){
            System.out.println("The number is present at the postition "+ i);
        }
        else{
            System.out.println("The number is not present in the array");
        }
    }
}