import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class FlaviusJosephus {

    void josephus(int numOfPeople, int n){
        List people = createListOfPeople(numOfPeople);
        List<Integer> deaths = new ArrayList<Integer>();
        while(people.size() > 0){
            Collections.rotate(people, -n);
            deaths.add((Integer) people.get(people.size() - 1));
            people.remove(people.size() - 1);
        }

        System.out.println(deaths.stream().map(String::valueOf)
        .collect(Collectors.joining(" ")));
    }

    List createListOfPeople(int numOfPeople){
        List<Integer> listOfPeople = new ArrayList<Integer>();

        for(int person = 0; person < numOfPeople; person++){
            listOfPeople.add(person);
        }

        return listOfPeople;
    }

    public static void main(String[] args) {
        FlaviusJosephus s = new FlaviusJosephus();
        s.josephus(5, 2);
    }
}
