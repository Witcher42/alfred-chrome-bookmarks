import re

class RankingList():
    @staticmethod
    def matches(queryTerms, things):
        for term in queryTerms:
            regexp = re.compile(re.escape(term), re.UNICODE | re.IGNORECASE)
            for thing in things:
                matched = not bool(regexp.search(thing))
                if matched:
                    return False

        return True

#matches: function() {
      #var matchedTerm, queryTerms, regexp, term, thing, things, _i, _j, _len, _len1;
      #queryTerms = arguments[0], things = 2 <= arguments.length ? __slice.call(arguments, 1) : [];
      #for (_i = 0, _len = queryTerms.length; _i < _len; _i++) {
        #term = queryTerms[_i];
        #regexp = RegexpCache.get(term);
        #matchedTerm = false;
        #for (_j = 0, _len1 = things.length; _j < _len1; _j++) {
          #thing = things[_j];
          #matchedTerm || (matchedTerm = thing.match(regexp));
        #}
        #if (!matchedTerm) {
          #return false;
        #}
      #}
      #return true;
    #},
