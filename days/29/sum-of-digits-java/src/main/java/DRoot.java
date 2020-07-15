public class DRoot {
    public static int digital_root(int n) {
        int sumOfDigits = 0;

        if (String.valueOf(n).length() == 1){
            return n;
        }

        for(char ch: String.valueOf(n).toCharArray()){
            sumOfDigits += Character.getNumericValue(ch);
        }

        return digital_root(sumOfDigits);
    }
}
