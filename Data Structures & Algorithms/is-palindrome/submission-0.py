class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(filter(str.isalnum,s)).lower()
        print(string)
        print(string[::-1])
        if string == string[::-1]:
            return True

        return False