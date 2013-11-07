public class TrafficCongestionDivTwo {
 
    public long theMinCars(int treeHeight) {
	if(treeHeight==1){
	    return 1;
	}
	
	long a1 = 1;
	long a2 = 1;
	
	int s = 2;
	while (s++ <= treeHeight) {
	    long a3 = 2 * a1 + a2;
	    a1 = a2;
	    a2 = a3;
	}
	
	return a2;
 
	//return rec(treeHeight); //タイムアウト
	//return prot(treeHeight);
    }
    
    public long rec(int s){
	if(s == 0) return 1;
	if(s == 1) return 1;
	return 2 * rec(s-2) + rec(s-1);
    }
    
    public long prot(int treeHeight){
	long[] s = new long[treeHeight+1];
	s[0] = 1;
	s[1] = 1;
	int i = 2;
	while(i <= treeHeight){
	    long sum = 1;
	    for (int j = 0; j < i-1; j++) {
		sum += s[j] * 2;
	    }
	    s[i++] = sum;
	}
	return s[treeHeight];
    }
}