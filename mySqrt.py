"""
https://leetcode-cn.com/problems/sqrtx/submissions/
二分法求平方根的整数部分
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        a = x
        b = 0
        if x == 0 or x == 1:
            return x
        while b<=a:
            temp = (a+b)//2
            if (temp**2)<=x:
                if ((temp+1)**2)>x:
                    return temp
                else:
                    b = temp+1
            else:
                a = temp-1


            