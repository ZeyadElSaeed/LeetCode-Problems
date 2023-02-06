class Solution:
    def average(self, salary: List[int]) -> float:
        min_sofar = salary[0]
        max_sofar = salary[0]
        salary_sum = 0
        
        for x in salary:
            min_sofar = min(min_sofar, x)
            max_sofar = max(max_sofar, x)
            salary_sum += x
            
        return (salary_sum - min_sofar - max_sofar) / (len(salary)-2)
            
        