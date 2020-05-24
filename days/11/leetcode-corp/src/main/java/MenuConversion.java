import java.awt.*;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.*;
import java.util.List;
import java.util.stream.Stream;

public class MenuConversion {

    HashMap<String, Integer> MENU = new HashMap<String, Integer>()
    {{
        put("Cappuccino", 0);
        put("Club Sandwich", 1);
        put("Green Salad", 2);
        put("Sparkling Water", 3);
    }};

    List<String[]> loadOrders(String fileName){
        List<String[]> orders = new ArrayList<>();
        File file = new File(
                Objects.requireNonNull(getClass().getClassLoader().getResource(fileName)).getFile()
        );

        try (Stream<String> lineStream = Files.lines(file.toPath())) {
            lineStream.forEach(line -> {
                orders.add(line.split(","));
            });
        } catch (IOException e) {
            e.printStackTrace();
        }

        return orders;
    }

    HashMap<Integer, Integer[]> convertOrdersToFoodItems(List<String[]> orders){
        HashMap<Integer, Integer[]> mapOfConvertedOrders = new HashMap<>();

        for(String[] order: orders){
            int tableNumber = Integer.parseInt(order[1]);
            String typeOfFood = order[2];

            if(!mapOfConvertedOrders.containsKey(tableNumber)){
                mapOfConvertedOrders.put(tableNumber, new Integer[]{0, 0, 0, 0});
            }
            mapOfConvertedOrders.get(tableNumber)[MENU.get(typeOfFood)] += 1;

        }
        return mapOfConvertedOrders;
    }

    void formatFoodItems(HashMap<Integer, Integer[]> mapOfConvertedOrders){

        mapOfConvertedOrders.forEach((key, value) -> System.out.println(key + " " + Arrays.toString(value)));

    }

    public static void main(String[] args) {
        MenuConversion s = new MenuConversion();
        List<String[]> ordersToBeConverted = s.loadOrders("input.txt");

        s.formatFoodItems(s.convertOrdersToFoodItems(ordersToBeConverted));

//        2 [0, 1, 0, 0]
//        5 [0, 0, 0, 1]
//        7 [1, 0, 1, 0]


    }
}