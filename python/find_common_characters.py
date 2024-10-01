"""
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
"""


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hm = Counter(words[0])

        for i in range(1, len(words)):
            hm_temp = Counter(words[i])
            for k in hm:
                hm[k] = min(hm[k], hm_temp[k])

        common = []
        for c in hm:
            for i in range(hm[c]):
                common.append(c)
        return common