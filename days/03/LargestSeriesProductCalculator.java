import java.util.ArrayList;
import java.util.List;

class LargestSeriesProductCalculator {

  String inputNumber;

  LargestSeriesProductCalculator(String inputNumber) {

    if(inputNumber.isEmpty() || inputNumber.matches("[0-9]+")){
      this.inputNumber = inputNumber;
    } else {
      throw new IllegalArgumentException("String to search may only contain digits.");
    }
  }

  long calculateLargestProductForSeriesLength(int numberOfDigits) {

    if(numberOfDigits > inputNumber.length()){
      throw new IllegalArgumentException("Series length must be less than or equal to the length of the string to search.");
    }
    if(numberOfDigits < 0){
      throw new IllegalArgumentException("Series length must be non-negative.");
    }
    if(inputNumber.length() == 0 || numberOfDigits == 0){
      return 1;
    }

    char[] inputNumberArray = inputNumber.toCharArray();
    long maxProduct = Long.MIN_VALUE;

    for(int i = 0; i < inputNumber.length() - numberOfDigits + 1; i++){
      List<Integer> subList = new ArrayList<>();
      subList.add(Character.getNumericValue(inputNumberArray[i]));

      for(int p = i + 1; p < i + numberOfDigits; p++){
        subList.add(Character.getNumericValue(inputNumberArray[p]));
      }
      maxProduct = Math.max(maxProduct, findProductOfSubstring(subList));
    }
    return maxProduct;
  }

  long findProductOfSubstring(List<Integer> subArray){
    long product = 1;

    for(long num: subArray){
      product *= num;
    }

    return product;
  }

}
