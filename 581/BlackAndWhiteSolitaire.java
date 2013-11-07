public class BlackAndWhiteSolitaire {
 
    public int minimumTurns(String cardFront) {
        String[] candidate = new String[] { "", "" };
 
        for (int i = 0; i < cardFront.length(); i++) {
            if (i % 2 == 0) {
                candidate[0] += "W";
                candidate[1] += "B";
            } else {
                candidate[0] += "B";
                candidate[1] += "W";
            }
        }
 
        int min = cardFront.length();
        for (int i = 0; i < candidate.length; i++) {
            int n = 0;
            for (int j = 0; j < cardFront.length(); j++) {
                if (candidate[i].charAt(j) != cardFront.charAt(j)) {
                    n++;
                }
            }
            min = Math.min(min, n);
        }
 
        return min;
    }
 
}