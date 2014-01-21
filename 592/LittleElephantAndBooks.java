import java.util.Arrays;

public class LittleElephantAndBooks {

    public int getNumber(int[] pages, int number) {
        int[] sorted = pages.clone();
        Arrays.sort(sorted);

        int ans = 0;
        for (int i = 0; i <= number; i++) {
            if (i != number - 1) {
                ans += sorted[i];
                System.out.print(ans + " ");
            }
        }
        
        System.err.println(ans);
        return ans;
    }

}
