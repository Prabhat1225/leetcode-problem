# You are given an integer array deck where deck[i] represents the number written on the ith card.
# Partition the cards into one or more groups such that:
# Each group has exactly x cards where x > 1, and
# All the cards in one group have the same integer written on them.
# Return true if such partition is possible, or false otherwise.
# Input: deck = [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        res=Counter(deck)
        a=list(res.values())
        if gcd(*a)>1:
            return 1
        else:
            return 0   