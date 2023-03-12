class Solution(object):
    def isAlienSorted(self, words, order):
        def compare(word1, word2, order):
            if word1 == word2:
                return True
            elif len(word1) < len(word2):
                for i in range(len(word1)):
                    if order.index(word1[i]) < order.index(word2[i]):
                        return True
                    elif order.index(word1[i]) > order.index(word2[i]):
                        return False
                return True
            elif len(word1) > len(word2):
                for i in range(len(word2)):
                    if order.index(word2[i]) < order.index(word1[i]):
                        return False
                    elif order.index(word2[i]) > order.index(word1[i]):
                        return True
                return False
            else:
                for i in range(len(word1)):
                    if order.index(word1[i]) < order.index(word2[i]):
                        return True
                    elif order.index(word1[i]) > order.index(word2[i]):
                        return False
        for i in range(0, len(words)-1):
            if compare(words[i], words[i+1], order) == False:
                return False
        return True
