import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class Array2DExercisesTest {

  private int[][] basic, allneg, nonsquare, negatives, rowmagic, colmagic,
      magic, notmagic1, notmagic2, latin, notlatin;

  @BeforeEach
  void setUp() {
    basic = new int[][] { {1,2,3}, {4,5,6}, {7,8,9} };
    allneg = new int[][] { {-10,-12,-3}, {-4,-5,-6,-8}, {-7,-8} }; //all neg and ragged
    nonsquare = new int[][] { {1,2,3}, {4,5}, {6,7,8,9} };
    negatives = new int[][] { {1,-2,3}, {4,5,6}, {-7,8,-9} };
    rowmagic = new int[][] { {1,2,3}, {-1,5,2}, {4,0,2} };
    colmagic = new int[][] { {1,-1,4,10}, {3,5,0,-6} };
    latin = new int[][] { {1,2,3}, {2,3,1}, {3,1,2} };
    notlatin = new int[][] { {2,1,3}, {2,3,1}, {3,1,2} };
    magic = new int[][] { {2,2,2}, {2,2,2}, {2,2,2}   };
    notmagic1 = new int[][] { {1,2,3}, {4,5,6}, {6,8,9} }; //diag sums are not equal
    notmagic2 = new int[][] { {1,5,3}, {4,5,6}, {7,8,9} }; //diag sums are equal but rows are not
  }

  /**
   * Test max is found correctly (last element in the search)
   */
  @Test
  void testMaxNormal() {
    assertEquals(9,Array2DExercises.max(basic));
  }

  /**
   * Test max correct when all vals are negative
   */
  @Test
  void testMaxAllNeg() {
    assertEquals(-3,Array2DExercises.max(allneg));
  }

  /**
   * Test row sum calculated correctly including for nonsquare arrays
   */
  @Test
  void testRowSum() {
      assertEquals(6, Array2DExercises.rowSum(basic, 0));
      assertEquals(15, Array2DExercises.rowSum(basic, 1));
      assertEquals(24, Array2DExercises.rowSum(basic, 2));
      assertEquals(30, Array2DExercises.rowSum(nonsquare, 2));
  }

  /**
   * Test column sum calculated correctly for standard cases
   */
  @Test
  void testColumnSum() {
      assertEquals(12, Array2DExercises.columnSum(basic, 0));
      assertEquals(15, Array2DExercises.columnSum(basic, 1));
      assertEquals(18, Array2DExercises.columnSum(basic, 2));
  }
}