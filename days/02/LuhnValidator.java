class LuhnValidator {

  boolean isValid(String candidate) {

    candidate = candidate.replaceAll(" ", "");

    if (candidate.length() <= 1){
      return false;
    }

    char[] candidateArray = candidate.toCharArray();
    int candidateSum = 0;

    for(int index = candidate.length() - 2; index >= 0; index-=2){

      int orig_num = Character.getNumericValue(candidateArray[index]);

      // Greater than 9 is non numeric char
      if(orig_num > 9){
        return false;
      }

      int double_orig_num = orig_num * 2;

      if (double_orig_num > 9){
        double_orig_num = double_orig_num - 9;
      }
      candidateArray[index] = Character.forDigit(double_orig_num, 10);
    }

    for(char num: candidateArray){
      candidateSum += Character.getNumericValue(num);
    }

    return candidateSum % 10 == 0;
  }

}