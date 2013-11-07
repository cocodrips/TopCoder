import java.util.HashSet;
 
public class AstronomicalRecordsEasy {
 
    public int minimalPlanets(int[] A, int[] B) {
        int min = A.length + B.length - 1;
 
        for (int a : A) {
            for (int b : B) {
                HashSet<Integer> set = new HashSet<Integer>();
                for (int ai = 0; ai < A.length; ai++) {
                    set.add(A[ai] * b);
                }
                for (int bi = 0; bi < B.length; bi++) {
                    if (min <= set.size()) {
                        break;
                    }
                    set.add(B[bi] * a);
                }
                min = set.size();
            }
        }
        return min;
    }
 
}