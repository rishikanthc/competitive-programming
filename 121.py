class Solution:
    def helper(self, b, s):
        if s >= self.n:
            return self.prices[b] - self.prices[s]
        if self.cache[s][b] != -1:
            return self.cache[s][b]

        profit = self.prices[s] - self.prices[b]
        self.cache[s][b] = profit

        return max(profit, self.helper(b+1, s+1))


    def maxProfit(self, prices):
        self.prices = prices
        self.n = len(prices) - 1
        self.cache = [[-1 for i in range(self.n)] for j in range(self.n)]
        if prices == []:
            return 0
        profit = self.helper(0,0)
        
        return profit

if __name__ == '__main__':
    solver = Solution()
    print(solver.maxProfit([7,1,5,3,6,4]))
    print(solver.maxProfit([7,6,4,3,1]))
