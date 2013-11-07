public class FoxAndClassroom {
 
    public String ableTo(int n, int m) {
        boolean[][] seated = new boolean[n][];
        for (int i = 0; i < seated.length; i++) {
            seated[i] = new boolean[m];
        }
 
        int r = 0;
        int c = 0;
        seated[r][c] = true;
        for (int i = 1; i < n * m; i++) {
            r = (r + 1) % n;
            c = (c + 1) % m;
            if (seated[r][c]) {
                return "Impossible";
            }
        }
        return "Possible";
    }
    
}