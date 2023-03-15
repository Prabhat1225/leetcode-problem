# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

#  Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m=len(text1)
        n=len(text2)
        f=[]
        for i in range(m+1):
            f.append([])
            for j in range(n+1):
                f[i].append(0)

        for i in range(m):
            for j in range(n):
                if  text1[i]==text2[j]:
                    f[i+1][j+1]=f[i][j]+1
                else:
                    f[i+1][j+1]=max(f[i][j+1],f[i+1][j])
        return f[m][n]                        
        
