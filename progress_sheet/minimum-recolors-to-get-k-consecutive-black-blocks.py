class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count=k
        for i in range(len(blocks)-k+1):
            black="B"*k
            if blocks[i:i+k]==black:
                return 0
            else:
                temp=blocks[i:i+k].count("W")
                if temp<count:
                    count=temp
        return count
        
                

        