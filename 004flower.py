class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        fb = [0] + flowerbed + [0]
        for i in range(1, len(fb)-1):
            if fb[i-1] == fb[i] == fb[i+1] == 0:
                fb[i] = 1
                n -= 1
                if n == 0: return True
        return n <= 0
