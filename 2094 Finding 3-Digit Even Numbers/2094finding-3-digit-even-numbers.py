class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        result  = []
        counter = Counter(digits)

        for last in counter.keys():
            if last % 2 == 1:
                continue

            counter[last] -= 1
            
            for first in counter.keys():
                if first == 0 or counter[first] == 0:
                    continue
                
                counter[first] -= 1

                for second in counter.keys():
                    if counter[second] == 0:
                        continue
                    result.append(first*100+second*10+last)
                    
                counter[first] += 1

            counter[last] += 1
        
        result.sort()
        return result