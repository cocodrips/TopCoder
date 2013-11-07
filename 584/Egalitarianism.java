import java.util.LinkedList;
import java.util.Queue;
 
public class Egalitarianism {
 
    public int maxDifference(String[] isFriend, int d) {    
	int mmax =  0;
	for (int s = 0; s < isFriend.length; s++) {
 
	    Queue<Integer> queue = new LinkedList<Integer>();
	    int[] step = new int[isFriend.length];
	    boolean[] visited = new boolean[isFriend.length];
      
	    queue.add(s);
	    visited[s] = true;
	    step[s] = 0;
	    while (!queue.isEmpty()) {
		int q = queue.poll();
		for (int i = 0; i < isFriend.length; i++) {
		    if(q == i) continue;
		    if(isFriend[q].charAt(i) == 'Y'){
			if(!visited[i]){
			    queue.add(i);
			    visited[i] = true;
			    step[i] = step[q] + 1; 
			}
		    }
		}
	    }
      
	    for (int i = 0; i < visited.length; i++) {
		if(!visited[i]){
		    return -1; 
		}
	    }
      
	    int max = 0;
	    for (int i = 0; i < step.length; i++) {
		if(step[i] > max){
		    max = step[i];
		}
	    }
	    mmax = Math.max(max, mmax);
	}
	return mmax * d;
    }
}