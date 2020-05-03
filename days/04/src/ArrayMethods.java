import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class ArrayMethods {

  int findMax(int[] arr){
    int maxNum = Integer.MIN_VALUE;

    for(int num: arr){
      if(num > maxNum){
        maxNum = num;
      }
    }
    return maxNum;
  }

  int findMin(int[] arr){
    int maxNum = Integer.MAX_VALUE;

    for(int num: arr){
      if(num < maxNum){
        maxNum = num;
      }
    }
    return maxNum;
  }

  String removeEvenNumbersFromArray(int[] arr){
    List<Integer> listOfOddNums = new ArrayList<Integer>();

    for(int num: arr){
      if(!(num % 2 == 0)){
        listOfOddNums.add(num);
        }
    }
    return Arrays.toString(listOfOddNums.toArray(new Integer[0]));
  }

  int[] removeEvenNumbersFromArrayReturnsArray(int[] arr){
    int count = 0;
    int index = 0;

    for (int num: arr){
      if(num % 2 == 1){
        count++;
      }
    }

    int[] arrayWithOddNums = new int[count];

    for(int num: arr){
      if(num % 2 == 1){
        arrayWithOddNums[index] = num;
        index++;
      }
    }
    return arrayWithOddNums;
  }

  public static void main(String[] args) {
    int[] sample = new int[] {3, 5, 1, 2, 8, 10, 44, 22};

    ArrayMethods s = new ArrayMethods();
    System.out.println(Arrays.toString(s.removeEvenNumbersFromArrayReturnsArray(sample)));

  }
}