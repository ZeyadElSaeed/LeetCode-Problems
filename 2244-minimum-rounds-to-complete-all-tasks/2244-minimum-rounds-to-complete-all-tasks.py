class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks = sorted(tasks)
        check = list()
        my_dictionary = dict()
        for task in tasks:
            if task in my_dictionary:
                my_dictionary[task] += 1
            else : 
                my_dictionary[task] = 1
        for k in my_dictionary:
            x = 0
            counts = my_dictionary[k]
            if (counts == 1):
                x = -1
            elif (counts % 3 == 0):
                x =  counts / 3
            else:
                division =  int(counts / 3)
                while True:
                    remain = counts - (division * 3)
                    if ( remain % 2 == 0) :
                        x =  division + (remain/2)
                        break
                    else:
                        division -= 1

            if x == -1:
                return x
            check.append(int(x))   
        return sum(check)        
        