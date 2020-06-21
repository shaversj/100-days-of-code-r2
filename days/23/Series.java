import java.util.ArrayList;
import java.util.List;

class Series {

    String stringOfNumbers;

    Series (String stringOfNumbers){
        this.stringOfNumbers = stringOfNumbers;
    }

    List<String> slices(int numOfSlice){

        if(numOfSlice <= 0){
            throw new IllegalArgumentException("Slice size is too small.");
        }
        if(numOfSlice > stringOfNumbers.length()){
            throw new IllegalArgumentException("Slice size is too big.");
        }

        ArrayList<String> al = new ArrayList<>();

        for(int i = 0; i < stringOfNumbers.length() - numOfSlice + 1; i++){
            StringBuilder sb = new StringBuilder();
            sb.append(stringOfNumbers.charAt(i));

            for(int p = i + 1; p < i + numOfSlice; p++){
                sb.append(stringOfNumbers.charAt(p));
            }
            al.add(sb.toString());
        }
        return al;
    }
}