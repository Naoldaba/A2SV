class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        h, w = len(matrix), len(matrix[0])
        
		
        for y in range(h):
            for x in range(1,w):
                matrix[y][x] = matrix[y][x] + matrix[y][x-1]
                
        counter = 0
        
        for left in range(w):
            for right in range(left, w):
                
                accumulation = defaultdict(int)
                accumulation[0]=1
                
                area = 0
                
                for y in range(h):
                    
                    if left > 0:
                        area += matrix[y][right] - matrix[y][left-1]
                    
                    else:
                        area += matrix[y][right]
                    
                    counter += accumulation[area-target]
                    
                    accumulation[area] = accumulation[area] + 1
        
        return counter