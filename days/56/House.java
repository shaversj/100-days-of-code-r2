class House{

    String[] endOfRhyme = {
            "the house that Jack built.",
            "the malt",
            "the rat",
            "the cat",
            "the dog",
            "the cow with the crumpled horn",
            "the maiden all forlorn",
            "the man all tattered and torn",
            "the priest all shaven and shorn",
            "the rooster that crowed in the morn",
            "the farmer sowing his corn",
            "the horse and the hound and the horn",
    };

    String[] startOfRhyme = {
            "that ate ",
            "that killed ",
            "that worried ",
            "that tossed ",
            "that milked ",
            "that kissed ",
            "that married ",
            "that woke ",
            "that kept ",
            "that belonged to ",
            " ",
    };

    String verse(int startVerse){
        StringBuilder sb = new StringBuilder();

        if (startVerse == 1){
            return "This is the house that Jack built.";
        }

        sb.append("This is ").append(endOfRhyme[startVerse - 1]).append(" ");

        for (int startRhymeIndex = startVerse - 3, endRhymeIndex = startVerse - 2; endRhymeIndex > 0; startRhymeIndex--, endRhymeIndex--){
            sb.append(startOfRhyme[startRhymeIndex]).append(endOfRhyme[endRhymeIndex]).append(" ");
        }

        sb.append("that lay in the house that Jack built.");

        return sb.toString().trim();
    }

    String verses(int startVerse, int endVerse){
        return "";
    }

    String sing(){
        return "";
    }
}
