'''
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

 

Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
 

Note:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
'''

class Solution:
    def longestStrChain(self, words):
        n = len(words)
        words.sort(key=len)
        cache = [1] * len(words)
        result = 0
        
        def check(w1, w2):
            if len(w1) != (len(w2) - 1):
                return 0
            flag = 1
            for i in w1:
                if i not in w2: flag = 0 
            return flag

        for i in range(n):
            j = i - 1

            while (j >= 0 and len(words[j]) >= (len(words[i]) - 1)):
                chk = check(words[j], words[i])

                if chk:
                    cache[i] = max(cache[i], 1 + cache[j])

                j -= 1
            if cache[i] > result:
                result = cache[i]

        return result

if __name__ == '__main__':
    solver = Solution()
    assert solver.longestStrChain(["a","b","ba","bca","bda","bdca"]) == 4
    assert solver.longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]) == 7
    assert solver.longestStrChain(["wnyxmflkf","xefx","usqhb","ttmdvv","hagmmn","tmvv","pttmdvv","nmzlhlpr","ymfk","uhpaglmmnn","zckgh","hgmmn","isqxrk","isqrk","nmzlhpr","uysyqhxb","haglmmn","xfx","mm","wymfkf","tmdvv","uhaglmmn","mf","uhaglmmnn","mfk","wnymfkf","powttkmdvv","kwnyxmflkf","xx","rnqbhxsj","uysqhb","pttkmdvv","hmmn","iq","m","ymfkf","zckgdh","zckh","hmm","xuefx","mv","iqrk","tmv","iqk","wnyxmfkf","uysyqhb","v","m","pwttkmdvv","rnqbhsj"]) == 10
