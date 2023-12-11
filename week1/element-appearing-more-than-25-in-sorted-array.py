class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        store=Counter(arr)
        print(store)
        for num, count in store.items():
            if count>len(arr)//4:
                return num
        