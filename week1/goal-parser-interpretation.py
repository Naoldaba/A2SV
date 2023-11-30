class Solution:
    def interpret(self, command: str) -> str:
        new_str=""
        for i in range(len(command)):
            if command[i]=="G":
                new_str+=command[i]
            elif command[i]=="(" and command[i+1]==")":
                new_str+="o"
            elif command[i]=="(" and command[i+1]=="a":
                new_str+="al"
            else: 
                pass
        return new_str
        
           
                
            
        