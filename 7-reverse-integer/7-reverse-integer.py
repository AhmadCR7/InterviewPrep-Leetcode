class Solution:
    def reverse(self, x: int) -> int:
        
        MIN = -2147483648
        MAX = 2147483647
        
        res = 0 
        
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x/10)
            
            if (res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10)):
                return 0
            if (res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10)):
                return 0
            res = (res*10) + digit 
        return res 
    
    '''
    we set our res = 0
    we chech for x while x:
we take x and mod it by 10 becuase of python since -1 % 10 = 0 
we use digit=int(math.fmod(x, 10))
now we take the x and divid by 10 x = int(x/10) we use int becuase python -1//10 = -1

we want the max value and devide by 10 except the last digit 
if (res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10)): it will over flow so we return 0 
if (res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10)): if the res is too small then return 0

now take the res  = (res*10) + digit 
return res 

Time Complexity: O(log(num))

Auxiliary Space: O(1)



    
    '''
        