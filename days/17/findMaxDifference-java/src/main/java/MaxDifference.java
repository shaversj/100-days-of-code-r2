public class MaxDifference {

    static int findMaxDifference(int[] listOfInts){
        int maxDifference = Integer.MIN_VALUE;

        for (int i = 0; i < listOfInts.length; i++){
            int difference = 0;
            for (int p = i + 1; p < listOfInts.length; p++){
                difference = listOfInts[p] - listOfInts[i];
                if (difference > maxDifference){
                    maxDifference = difference;
                }

            }
        }
        return maxDifference;
    }
}
