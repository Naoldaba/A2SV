class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.life_span=timeToLive
        self.token_set=defaultdict(int)
    def generate(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.token_set:
            self.token_set[tokenId]=currentTime
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token_set and self.token_set[tokenId]+self.life_span>currentTime:
            self.token_set[tokenId]=currentTime
        elif tokenId in self.token_set:
            del self.token_set[tokenId]
    def countUnexpiredTokens(self, currentTime: int) -> int:
        result=[]
        for Id, ct in self.token_set.items():
            if ct+self.life_span>currentTime:
                result.append(Id)
        return len(result)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)