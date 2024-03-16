#User function Template for python3
class Solution:
    def getLastDigit(self, a, b):
        a,b=int(a),int(b)
        if b==0:
            return 1
        elif b%4==0:
            return (a**4)%10
        else:
            exp=b%4
            return (a**exp)%10
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b=map(str,input().split())
        
        ob = Solution()
        print(ob.getLastDigit(a,b))
# } Driver Code Ends