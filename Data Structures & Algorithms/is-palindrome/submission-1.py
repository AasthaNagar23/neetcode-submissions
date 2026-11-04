class Solution:
    def isPalindrome(self, s: str) -> bool:
        f=""
        for i in s:
            if (i.isdigit() or i.isalpha()) and i!=" ":
                f+=i
        a=f.lower()
        if a[::-1]==a:
            return True
        else:
            return False


        
      