import java.awt.print.Printable;
import java.util.Arrays;
import java.util.Iterator;

public class LittleElephantAndPermutationDiv2 {

	public long getNumber(int N, int K) {
	    long combination = 0;
	    long ans = 0;
        for(int[] permutation : new Permutation(N)) {
            int sum = 0;
            for (int i = 0; i < permutation.length; i++) {
                int max = Math.max(permutation[i] + 1, i + 1);
                sum += max;
            }
            if (sum >= K) {
                ans ++;
            }
            combination++;
        }
	    return ans * combination;
	   
	}
	
	public class Permutation implements Iterable<int[]> {
	    private final int size;
	    public Permutation(int size) {
	        if (size <= 0) throw new IllegalArgumentException();
	        this.size = size;
	    }

	    public Iterator<int[]> iterator() {
	        return new Iter(size);
	    }

	    private class Iter implements Iterator<int[]> {
	        private final int[] source;
	        private boolean isFirst = true;

	        private Iter(int size) {
	            source = new int[size];
	            for(int i = 0; i < size; ++i) {
	                source[i] = i;
	            }
	        }

	        public boolean hasNext() {
	            if (isFirst) {
	                isFirst = false;
	                return true;
	            }

	            int n = source.length;
	            for (int i = n - 1; i > 0; i--) {
	                if (source[i - 1] < source[i]) {
	                    int j = n;
	                    while (source[i - 1] >= source[--j]);
	                    swap(source, i - 1, j);
	                    reverse(source, i, n);
	                    return true;
	                }
	            }
	            reverse(source, 0, n);
	            return false;
	        }

	        public int[] next() {
	            return source;
	        }

	        public void remove() {
	            throw new UnsupportedOperationException();
	        }

	        private void swap(int[] is, int i, int j) {
	            int t = is[i];
	            is[i] = is[j];
	            is[j] = t;
	        }

	        private void reverse(int[] is, int s, int t) {
	            while (s < --t) swap(is, s++, t);
	        }
	    }
	}
}
