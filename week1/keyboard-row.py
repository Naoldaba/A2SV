class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        output=[]
        set1 = {'q','w','e','r','t','y','u','i','o','p'}
        set2 = {'a','s','d','f','g','h','j','k','l'}
        set3 = {'z','x','c','v','b','n','m'}
        for word in words:
            word_set=set(word.lower())
            if (set1.union(word_set)==set1) or (set2.union(word_set)==set2) or (set3.union(word_set)==set3):
                output.append(word)
        return output