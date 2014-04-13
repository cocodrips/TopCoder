import math
import string

class BoundingBox:
    def smallestArea(self, X, Y):
        minS = 100000000000000000000
        X = list(X)
        Y = list(Y)
        mostR = -1000000000000000000
        mostL = 1000000000000000000
        mostT = -1000000000000000000
        mostD = 1000000000000000000

        for x, y in zip(X, Y):
            mostR = max(mostR, x)
            mostL = min(mostL, x)
            mostT = max(mostT, y)
            mostD = min(mostD, y)
        
        return abs((mostR - mostL) * (mostT - mostD))


#Powered by KawigiEdit-pfx 2.1.9!
