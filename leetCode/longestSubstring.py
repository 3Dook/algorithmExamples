class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length =0
        i = 0
        j = 0
        temp = []
        
        while(i < len(s) and j < len(s)):
            #print(temp)
            if( s[j] not in temp):
                # add to temp
                temp.append(s[j])
                j+=1
                length = max(length, j-i)
            else:
                i+=1
                temp.pop(0)
                
        return length