class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = []
        normals = []
        for i in range(len(s)):
            if s[i] !='a' and s[i] !='e' and s[i] !='i' and s[i] !='o' and s[i] !='u'and s[i] !='A' and s[i] !='E' and s[i] !='I' and s[i] !='O' and s[i] !='U':
                normals.append(s[i])
            else:
                normals.append(False)
                vowels.append(s[i])
        vowels = vowels[::-1]
        pos = 0 
        for i in range(len(normals)):
            if normals[i] == False:
                normals[i] = vowels[pos]
                pos+=1
        
        return "".join(normals)
