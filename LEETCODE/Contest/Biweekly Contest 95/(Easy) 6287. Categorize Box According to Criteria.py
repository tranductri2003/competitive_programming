class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """

        bulky = False
        if length >= 10**4 or width >= 10**4 or height >= 10**4 or length*width*height >= 10**9:
            bulky = True
        heavy = False
        if mass >= 100:
            heavy = True
        if heavy == True and bulky == True:
            return "Both"
        elif heavy == False and bulky == False:
            return "Neither"
        elif bulky == True and heavy == False:
            return "Bulky"
        elif heavy == True and bulky == False:
            return "Heavy"
