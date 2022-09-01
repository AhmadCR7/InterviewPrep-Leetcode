class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
        
            res[tuple(count)].append(s)
        return res.values()
   
        
        
    
'''
we use hashmap 
we count the char of each 
create hashmap res = defaultdict(list)
go trough for s in strs:
count = [0] * 26

now go throgh every char s ->  for c in s:
count[ord(c) - ord('a')] += 1

a =  80 -> 0, 80 -80
b = 81 -> 1, 81 -80

now we want to append string s to the count res[count].append(s)
we have to change to tuple in python res[tuples(count)].append(s)

we dont want the keys just return the val 
return res.values()




time: o(m*n) where is m the number of char and n is the avg lenght of a string
'''