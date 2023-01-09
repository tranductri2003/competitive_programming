class DataStream(object):

    def __init__(self, value, k):
        """
        :type value: int
        :type k: int
        """
        self.value = value
        self.k = k
        self.data = []
        self.cur = 0

    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == self.value:
            self.cur += 1
            if self.cur >= self.k:
                return True
            else:
                return False
        else:
            self.cur = 0
            return False


t = DataStream(1, 2)
print(t.consec(1))
print(t.consec(2))
print(t.consec(1))
print(t.consec(1))
print(t.consec(2))
print(t.consec(1))
print(t.consec(1))
