import java.util.ArrayList;
import java.util.Collections;

public class EnoughIsEnough {
    public static int[] deleteNth(int[] elements, int maxOccurrences) {
        ArrayList<Integer> al = new ArrayList<>();

        for(int num: elements){
            if (Collections.frequency(al, num) < maxOccurrences){
                al.add(num);
            }
        }

        return al.stream().mapToInt(i -> i).toArray();
    }
}
