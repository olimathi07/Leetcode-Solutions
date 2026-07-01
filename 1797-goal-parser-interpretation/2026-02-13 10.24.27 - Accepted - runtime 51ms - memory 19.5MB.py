class Solution:
    def interpret(self, command: str) -> str:
        l=""
        for i in range(len(command)):
            if command[i]=='(' and command[i+1]==')':
                l+='o'
            if command[i].isalpha():
                l+=command[i]
        return l