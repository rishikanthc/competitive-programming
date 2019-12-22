class Solution:
    def helper(self, s, d):
        if (s+1) >= d:
            return 1

        if self.cache[s+1][d] != -1:
            return self.cache[s+1][d]

        one_jump = 0  + self.helper(s+1, d)
        two_jump = 0 + self.helper(s+2, d)
        
        self.cache[s+1][d] = one_jump + two_jump

        return self.cache[s+1][d]

    def climbStairs(self, n):
        self.cache = [[-1 for i in range(n)] for j in range(n)]
        ret = self.helper(-1, n-1)
        return ret

if __name__ == '__main__':
    solver = Solution()

    assert solver.climbStairs(2) == 2
    assert solver.climbStairs(3) == 3
    assert solver.climbStairs(4) == 5
