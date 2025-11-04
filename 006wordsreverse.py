class Solution(object):
    def reverseWords(self, s):

        s = s.strip()
        

        words = s.split()
        

        words.reverse()
        

        return " ".join(words)