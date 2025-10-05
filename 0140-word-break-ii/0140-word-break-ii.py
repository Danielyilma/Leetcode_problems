class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        words = []
        w_dict = set(wordDict)

        def recurse(idx, sent, leng):
            new_word = ""

            if leng == len(s):
                words.append(sent.strip())
                return

            if idx >= len(s):
                return

            for i in range(idx, len(s)):
                new_word += s[i]
                if new_word in w_dict:
                    new_sent = sent + " " + new_word
                    recurse(i + 1, new_sent, leng + len(new_word))
            

        recurse(0, "", 0)
        return words




        
        