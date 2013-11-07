public class PiecewiseLinearFunctionDiv2 {
 
    public int[] countSolutions(int[] Y, int[] query) {
	int[] ans = new int[query.length];
	for (int q = 0; q < query.length; q++) {
	    int n = 0;
	    if (query[q] == Y[Y.length-1]) {
		n++;
	    }
	    for (int y = 0; y < Y.length-1; y++) {
		if (Y[y] == query[q] && Y[y+1] == query[q]) {
		    n = -1;
		    break;
		}
		if ((Y[y] <= query[q] && query[q] < Y[y+1]) ||
		    (Y[y] >= query[q] && query[q] > Y[y+1])) {
		    n++;
		}
	    }
	    ans[q] = n;
	}
	return ans;
    }
 
}