class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr=[0]*1001
        for seats, start, end in trips:
            if seats > capacity: return False
            arr[start]+=seats
            arr[end]-=seats
        for i in range(1,len(arr)):
            arr[i]+=arr[i-1]
            if arr[i]>capacity: 
                return False
        return True
        