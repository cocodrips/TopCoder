import java.util.ArrayList;
import java.util.List;
 
public class WolfDelaymaster {
 
    public String check(String str) {
        String wolf = "wolf";
 
        List<String> validWordsList = new ArrayList<String>();
        for (int i = 1; i <= 12; i++) {
            String s = new String();
            for (int j = 0; j < 4; j++) {
                for (int w = 0; w < i; w++) {
                    s += wolf.charAt(j);
                }
            }
            validWordsList.add(s);
        }
 
        for (int i = 0; i < validWordsList.size(); i++) {
            str = str.replaceAll(validWordsList.get(i), ".");
        }
 
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) != '.') {
                return "INVALID";
            }
        }
 
        return "VALID";
 
    }
 
}