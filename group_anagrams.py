class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram={}
        for i in strs:
            sort="".join(sorted(i))
            if sort not in anagram:
                anagram[sort]=[]
            anagram[sort].append(i)
        return list(anagram.values())