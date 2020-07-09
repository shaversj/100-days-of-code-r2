public class WhoLikes {

    public static String whoLikesIt(String... names){

        String stringOfNames = "";
        int nameCounter = 0;
        for(String name: names){
            if (names.length == 2 && nameCounter == 1){
                stringOfNames += " and" + " " + name;
                break;
            }
            if(names.length == 3 && nameCounter == 1){
                stringOfNames += ", " + name + " and ";
                nameCounter += 1;
                continue;
            }
            if(names.length > 3 && nameCounter == 1) {
                stringOfNames += ", " + name + " and " + (names.length - nameCounter - 1) + " others";
                break;
            }
            else {
                stringOfNames += name;
                nameCounter += 1;
            }
        }
        return names.length == 0 ? "no one likes this" :
                names.length == 1 ? stringOfNames + " " + "likes this" : stringOfNames + " " + "like this";
    }

}
