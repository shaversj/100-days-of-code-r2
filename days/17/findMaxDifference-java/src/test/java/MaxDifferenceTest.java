import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class MaxDifferenceTest {

    @Test
    void findMaxDifference() {
        MaxDifference s = new MaxDifference();
        //int[] arr1 = new int[] {2, 3, 10, 6, 4, 8, 1};
        assertEquals(7, MaxDifference.findMaxDifference(new int[] {2, 7, 9, 5, 1, 3, 5}));
    }
}