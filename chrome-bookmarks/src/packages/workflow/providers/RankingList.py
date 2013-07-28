import re

class RankingList():
    @staticmethod
    def matches(queryTerms, things):
        for term in queryTerms:
            regexp = re.compile(re.escape(term), re.UNICODE | re.IGNORECASE)
            matched = False
            for thing in things:
                if not matched:
                    matched = bool(regexp.search(thing))
            if not matched:
                return False

        return True

    @staticmethod
    def wordRelevancy(queryTerms, things):
        queryLength = 0
        scores = [ 0.000000 for x in range(len(things))]
        for term in queryTerms:
            queryLength += len(term)
            for i, thing in enumerate(things):
                if len(thing) and RankingList.matches([term], [thing]):
                    scores[i] += 1

        finalScore = []

        for i, score in enumerate(scores):
            if len(things[i]):
                score = score / len(queryTerms)
                score = score * RankingList.normalizeDifference(queryLength, len(things[i]))
                finalScore.append(score)

        if len(finalScore):
            return sum(finalScore) / len(finalScore)
        else:
            return 0

    @staticmethod
    def normalizeDifference(a, b):
        big = max(a, b)
        return ((big - abs(a - b)) + 0.0) / big
