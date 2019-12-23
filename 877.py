class Solution:
    def stoneGame(self, piles):
        self.cache = [[-1 for j in piles] for i in piles]
        def helper(b, e):
            if b > e:
                return 0
            if self.cache[b][e] != -1:
                return self.cache[b][e]
            self.cache[b][e] = max(helper(b+1, e) + piles[b],
                        helper(b, e - 1) + piles[e])
            
            return self.cache[b][e]
            
        res = helper(0, len(piles)-1)
        return res > (sum(piles) - res)

if __name__ == '__main__':
    solver = Solution()
    assert solver.stoneGame([5,3,4,5]) == True
