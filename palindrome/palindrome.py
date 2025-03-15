class Solution(object):
    def is_palidrome(self, word:str)-> bool:
        word = word.lower() 
        for i in range(len(word)):
            if word[i]!=word[len(word)- 1-i]:
                return False
        return True


solution = Solution()
string = "palindrome"
print(solution.is_palidrome(string))
 