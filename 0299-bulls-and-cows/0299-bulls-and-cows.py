class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        my_dict = {}
        bulls_number = 0
        cows_number = 0
        
        for x,y in zip(secret, guess):
            if x == y:
                bulls_number += 1
                my_dict[x] = my_dict.get(x, 0) - 1
            my_dict[x] = my_dict.get(x, 0) + 1
            
        
        for x,y in zip(secret, guess):
            if x!=y and y in my_dict and my_dict[y] > 0:
                cows_number += 1
                my_dict[y] -= 1   
        
        return str(bulls_number) + 'A' + str(cows_number)  + 'B'
                    
            
        