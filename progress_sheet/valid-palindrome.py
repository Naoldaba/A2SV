class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string=""
        for i in s:
            if not i.isalnum():
                new_string+=""
            else:
                i=i.lower()
                new_string+=i
        rev_string=new_string[::-1]
        if rev_string==new_string:
            return True
        return False
        