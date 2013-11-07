public class KeyDungeonDiv2 {
 
    public int countDoors(int[] doorR, int[] doorG, int[] keys) {
	int open = 0;
	for (int i = 0; i < doorR.length; i++) {
	    int r = doorR[i];
	    int g = doorG[i];
	    int w = keys[2];
            r = r - keys[0];
            g = g - keys[1];
            if (r > 0) w -= r;
            if (g > 0) w -= g;           
            if (w >= 0) open ++;
        }
	return open;
    }
 
}