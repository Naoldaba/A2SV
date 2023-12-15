class ATM:

    def __init__(self):
        self.banknotes=[0]*5
        self.denominations=[20,50,100,200,500]

    def deposit(self, banknotesCount: List[int]) -> None:
       for i in range(len(banknotesCount)):
           self.banknotes[i]+=banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        output=[0]*5
        for i in range(len(self.banknotes)-1,-1,-1):
            notes, denom = self.banknotes[i], self.denominations[i]
            if denom > amount:
                continue
            notes_can_take=min(notes, amount//denom)
            amount-=notes_can_take*denom
            output[i]=notes_can_take
        if amount>0:
            return [-1]
        for i in range(len(output)):
            self.banknotes[i]-=output[i]
        return output


        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)