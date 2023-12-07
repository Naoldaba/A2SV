class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        looser_dic=defaultdict(int)
        result=[]
        for i in range(len(matches)):
          looser_dic[matches[i][1]]+=1

        loose_list=[]
        win_list=[]
        for i in range(len(matches)):
          win_list.append(matches[i][0])
          loose_list.append(matches[i][1])
        winner=list(set(win_list)-set(loose_list))
        winner=sorted(winner)
        result.append(winner)

        looser=[]
        for i in looser_dic:
          if looser_dic[i]==1:
            looser.append(i)
        looser=sorted(looser)
        result.append(looser)

        return result
        

        
        