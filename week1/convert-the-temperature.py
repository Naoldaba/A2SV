class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin=celsius+273.15
        fahranheit=celsius*1.8 + 32.0
        return [kelvin, fahranheit]