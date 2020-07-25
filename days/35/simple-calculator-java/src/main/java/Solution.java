import java.util.Stack;

public class Solution {

    public static int calculate(String s){
        int sign = 1; // 1 or -1 ...1 = positive number... -1 = negative number
        int sum = 0;
        Stack<Integer> stack = new Stack<Integer>();

        for(int i = 0; i < s.length(); i++){
            // number
            if (Character.isDigit(s.charAt(i))){
                // 0-9 or 999
                // get full number
                int num = 0;
                while (i < s.length() && Character.isDigit(s.charAt(i))){
                    // expanding the number by 10 during each rotation
                    num = num * 10 + Character.getNumericValue(s.charAt(i));
                    i++;
                    System.out.println(num);
                }
                sum += num * sign;
                i--;
            } else if (s.charAt(i) == '+'){
                sign = 1;
            } else if (s.charAt(i) == '-'){
                sign = -1;
            } else if (s.charAt(i) == '('){
                stack.push(sum);
                stack.push(sign);
                sum = 0;
                sign = 1;
            } else if (s.charAt(i) == ')') {
                sum = stack.pop() * sum;
                sum += stack.pop();
            }

        }

        return sum;
    }

    public static void main(String[] args) {
        int s = calculate("250-144");
        System.out.println(s);
    }
}
