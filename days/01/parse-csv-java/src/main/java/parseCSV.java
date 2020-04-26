import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class parseCSV {

    List<String[]> readCSVFile(String filePath) throws FileNotFoundException {
        List<String[]> parsedData = new ArrayList<>();
        // create a reader
        try (BufferedReader br = Files.newBufferedReader(Paths.get(filePath))) {

            String line;

            // Skip header
            line = br.readLine();

            while ((line = br.readLine()) != null) {

                String[] row = line.split(",");
                parsedData.add(row);
            }
        } catch (IOException ex) {
            throw new FileNotFoundException();
        }
        return parsedData;
    }

    String[] find_team_with_smallest_difference(List<String[]> data){
        Integer smallest_difference = Integer.MAX_VALUE;
        String team_with_smallest_difference = "";

        for(String[] entry: data){
            String current_team_name = entry[0];
            Integer goals = Integer.valueOf(entry[5]);
            Integer goals_allowed = Integer.valueOf(entry[6]);
            Integer current_difference = Math.abs(goals - goals_allowed);

            if (current_difference < smallest_difference){
                smallest_difference = current_difference;
                team_with_smallest_difference = current_team_name;
            }
        }
        return new String[] {team_with_smallest_difference, String.valueOf(smallest_difference)};
    }

    public static void main(String[] args) throws FileNotFoundException, URISyntaxException {
        URL csvPath = parseCSV.class.getResource("football.csv");
        parseCSV s = new parseCSV();
        System.out.println(csvPath.toString());
        List<String[]> data = s.readCSVFile(Paths.get(csvPath.toURI()).toFile().toString());
        System.out.println(Arrays.toString(s.find_team_with_smallest_difference(data)));
    }
}
