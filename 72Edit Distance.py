# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
 
 class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        table=[[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            table[i][0]=i
        for j in range(1,n+1):
            table[0][j]=j

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    table[i][j]=table[i-1][j-1]
                else:
                    table[i][j]=1+min(table[i-1][j] , table[i][j-1], table[i-1][j-1])
        return table[-1][-1]
         

                      
