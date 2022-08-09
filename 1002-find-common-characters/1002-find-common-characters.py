class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) < 2:
            return words 
        res = []
        alist = set(words[0])
        for one in alist:
            n = min(a_word.count(one) for a_word in words)
            if n:
                res += [one]*n
        return res 
        