import java.util.Arrays;

public class Array2DExercises {

  static int max(int[][] arr){
    int maxNum = Integer.MIN_VALUE;

    for(int[] row: arr){
      for(int value: row){
        if(value > maxNum){
          maxNum = value;
        }
      }
    }
    return maxNum;
  }

  static int rowSum(int[][] arr, int indexOfArray){
    return Arrays.stream(arr[indexOfArray]).sum();
  }

  static int columnSum(int[][] arr, int column){
    int sumOfColumn = 0;

    for(int[] row: arr){
      sumOfColumn += row[column];
    }

    return sumOfColumn;
  }

}
