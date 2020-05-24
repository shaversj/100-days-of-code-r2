import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;

public class OpenFile {

    void openFile(String fileName){
        // Gets file from resource folder
        File file = new File(
                Objects.requireNonNull(getClass().getClassLoader().getResource(fileName)).getFile()
        );

        try {
            List<String> lines = Files.readAllLines(file.toPath());

            for(String line: lines){
                System.out.println(Arrays.toString(line.split(",")));
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        OpenFile s = new OpenFile();
        s.openFile("input.txt");
    }
}
