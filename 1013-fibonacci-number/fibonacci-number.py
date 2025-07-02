class Solution(object):
    def fib(self, n):
        def f(n):
           
            if n==0 or n==1:
                return n
            return f(n-1)+f(n-2)
        return f(n)