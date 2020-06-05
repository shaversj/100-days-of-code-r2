public class BitPositions {

    static void isBitsSame(Integer n, Integer p1, Integer p2){
        String nBinaryVersion = Integer.toBinaryString(n);
        System.out.println(nBinaryVersion);

        // 1 based
        // The index of the bit starts at the end and begins with 1.
        int p1BitPosition = nBinaryVersion.length() - p1;
        int p2BitPosition = nBinaryVersion.length() - p2;

        System.out.println("P1 Bit: " + nBinaryVersion.charAt(p1BitPosition));
        System.out.println("P2 Bit: " + nBinaryVersion.charAt(p2BitPosition));
    }

    public static void main(String[] args) {
        isBitsSame(23, 2, 4);
    }
}
