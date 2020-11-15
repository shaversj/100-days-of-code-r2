import java.time.LocalDate;
import java.time.LocalDateTime;

public class Gigasecond {

    // Exercism
    // https://exercism.io/my/solutions/c00cf98f3bcc4902bd863718e1524798

    LocalDateTime dt;
    double gigaSecond = Math.pow(10, 9);

    public Gigasecond(LocalDate moment) {
        this.dt = moment.atStartOfDay();
    }

    public Gigasecond(LocalDateTime moment) {
        this.dt = moment;
    }

    public LocalDateTime getDateTime() {
        return dt.plusSeconds((long) gigaSecond);
    }

}