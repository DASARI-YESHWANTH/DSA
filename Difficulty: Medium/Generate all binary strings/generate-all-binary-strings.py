#User function Template for python3

class Solution:
    def solve(self,index,flag,numbers,result):
        if index>= len(numbers):
            result.append("".join(numbers))
            return
        numbers[index]='0'
        self.solve(index+1,True,numbers,result)
        if flag==True:
            numbers[index]='1'
            self.solve(index+1,False,numbers,result)
            numbers[index]='0'
    def generateBinaryStrings(self, n):
        numbers=['0']*n
        result=[]
        self.solve(0,True,numbers,result)
        return result
        
# class Solution:
#     def solve(self, index, flag, numbers, result):
#         if index >= len(numbers):
#             result.append("".join(numbers))
#             return
        
#         # Place '0' at the current index and proceed
#         numbers[index] = '0'
#         self.solve(index + 1, True, numbers, result)
        
#         # Place '1' only if the previous character was not '1'
#         if flag:
#             numbers[index] = '1'
#             self.solve(index + 1, False, numbers, result)
#             numbers[index] = '0'  # backtrack (optional since overwritten in the next step)
    
#     def generateBinaryStrings(self, n):
#         numbers = ['0'] * n
#         result = []
#         self.solve(0, True, numbers, result)
#         return result
