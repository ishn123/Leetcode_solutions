class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m1 = {}
        
        for ch in magazine:
            if ch in m1:
                m1[ch] += 1
            else:
                m1[ch] = 1
                
        for ch in ransomNote:
            if ch not in m1:
                return False
            
            m1[ch] -= 1
            if m1[ch] == 0:
                m1.pop(ch)
                
        return True
    
    
        