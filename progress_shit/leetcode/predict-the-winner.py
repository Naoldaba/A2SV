class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def game(rem_arr, turn, score1, score2):
            if not rem_arr:
                return score1>=score2
            
            choice1=game(
                rem_arr[1:],
                2 if turn == 1 else 1,
                score1 + rem_arr[0] if turn == 1 else score1,
                score2 + rem_arr[0] if turn == 2 else score2
            )

            choice2=game(
                rem_arr[:-1],
                2 if turn == 1 else 1,
                score1 + rem_arr[-1] if turn == 1 else score1,
                score2 + rem_arr[-1] if turn == 2 else score2
            )

            if turn == 1:
                return choice1 or choice2

            return choice1 and choice2

            
        return game(nums, 1, 0, 0)
        