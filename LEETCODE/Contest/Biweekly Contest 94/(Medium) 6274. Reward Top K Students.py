from collections import defaultdict


class Solution(object):
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        """
        :type positive_feedback: List[str]
        :type negative_feedback: List[str]
        :type report: List[str]
        :type student_id: List[int]
        :type k: int
        :rtype: List[int]
        """
        positive = defaultdict(lambda: False)
        for tu in positive_feedback:
            positive[tu] = True

        negative = defaultdict(lambda: False)
        for tu in negative_feedback:
            negative[tu] = True

        res = []
        for i in range(len(student_id)):
            score = 0
            data = report[i].split(" ")
            for tu in data:
                if positive[tu]:
                    score += 3
                if negative[tu]:
                    score -= 1
            res.append((student_id[i], score))

        res = sorted(res, key=lambda x: (-x[1], x[0]))
        ans = []
        for i in range(k):
            ans.append(res[i][0])
        return ans


t = Solution()
print(t.topStudents(["smart", "brilliant", "studious"], ["not"], [
    "this student is studious", "the student is smart"], [1, 2], 2))
