public class TheArithmeticProgression {

    public double minimumChange(int a, int b, int c) {
        double ans = (double)b  - ((double)(c + a) / 2.0);
        System.out.println(ans);
        return Math.abs(ans);
    }

}
