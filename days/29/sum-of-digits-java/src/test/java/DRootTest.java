import static org.junit.jupiter.api.Assertions.*;

class DRootTest {

    @org.junit.jupiter.api.Test
    void digital_root() {
        assertEquals( 7, DRoot.digital_root(16));
        assertEquals( 6, DRoot.digital_root(456));

    }
}