import static org.junit.jupiter.api.Assertions.*;

class WhoLikesTest {

    @org.junit.jupiter.api.Test
    void callWithEmptyString() {
        String expected = "no one likes this";
        String[] emptyArray = new String[0];
        assertEquals(expected, WhoLikes.whoLikesIt(emptyArray));
    }

    @org.junit.jupiter.api.Test
    void callWithOneName(){
        String expected = "Peter likes this";
        String[] oneNameArray = new String[1];
        oneNameArray[0] = "Peter";

        assertEquals(expected, WhoLikes.whoLikesIt(oneNameArray));
    }

    @org.junit.jupiter.api.Test
    void callWithTwoNames(){
        String expected = "Jacob and Alex like this";
        String[] twoNameArray = new String[2];
        twoNameArray[0] = "Jacob";
        twoNameArray[1] = "Alex";

        assertEquals(expected, WhoLikes.whoLikesIt(twoNameArray));
    }

    @org.junit.jupiter.api.Test
    void callWithThreeNames(){
        String expected = "Max, John and Mark like this";
        String[] threeNameArray = new String[3];
        threeNameArray[0] = "Max";
        threeNameArray[1] = "John";
        threeNameArray[2] = "Mark";

        assertEquals(expected, WhoLikes.whoLikesIt(threeNameArray));
    }

    @org.junit.jupiter.api.Test
    void callWithFourNames(){
        String expected = "Alex, Jacob and 2 others like this";
        String[] fourNameArray = new String[4];
        fourNameArray[0] = "Alex";
        fourNameArray[1] = "Jacob";
        fourNameArray[2] = "Mark";
        fourNameArray[3] = "Max";

        assertEquals(expected, WhoLikes.whoLikesIt(fourNameArray));
    }

    @org.junit.jupiter.api.Test
    void callWithFiveNames(){
        String expected = "Alex, Jacob and 3 others like this";
        String[] fiveNameArray = new String[5];
        fiveNameArray[0] = "Alex";
        fiveNameArray[1] = "Jacob";
        fiveNameArray[2] = "Mark";
        fiveNameArray[3] = "Max";
        fiveNameArray[4] = "Bob";

        assertEquals(expected, WhoLikes.whoLikesIt(fiveNameArray));
    }
}